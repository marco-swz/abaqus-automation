import pyarrow as pa
import pyarrow.dataset as ds
import pyarrow.parquet as pq
from pyarrow.interchange import from_dataframe
import json
import polars as pl
import numpy as np
import pickle
import gzip
import sqlite3
from dataclasses import dataclass

@dataclass
class Dataset:
    steps: ... 
    frames: ...
    types: ...
    nodes: ...

    def write_parquet(self, dir: str):
        self.steps.write_parquet(dir+'/steps.parquet')
        self.frames.write_parquet(dir+'/frames.parquet')
        self.types.write_parquet(dir+'/types.parquet')
        self.nodes.write_parquet(dir+'/nodes.parquet')

def read_data(path: str) -> dict:
    file = open(path)
    data = json.load(file)
    file.close()
    return data

def to_table(data: dict) -> pl.DataFrame:
    table = [];
    for step_name, step in data.items():
        for frame_num, frame in step.items():
            for val_type, nodes in frame.items():
                for node in nodes:
                    node_padded = [np.NaN]*6
                    if isinstance(node, float):
                        node = [node]
                    node_padded[:len(node)] = node

                    row = [
                        step_name,
                        frame_num,
                        val_type,
                    ] + node_padded

                    table.append(row)
    col_names = ['step_name', 'frame_num', 'val_type', 'val1', 'val2', 'val3', 'val4', 'val5', 'val6']
    return pl.DataFrame(table, col_names)

def to_dataset(data) -> Dataset:
    table_steps = []
    table_nodes = []
    table_frames = []
    types_unique = {}
    types_id = -1
    for step_id, step_name in enumerate(data.keys()):
        table_steps.append([step_id, step_name])
        step = data[step_name]

        for frame_id, frame_num in enumerate(step.keys()):
            table_frames.append([frame_id, step_id, frame_num])

            for node_type, nodes in step[frame_num].items():
                type_id = types_unique.get(node_type)
                if type_id is None:
                    types_id += 1
                    types_unique[node_type] = types_id
                    type_id = types_id

                for node_id, node in enumerate(nodes):
                    node_padded = [node_id, type_id, frame_id] + [np.NaN]*5
                    if isinstance(node, float):
                        node = [node]
                    node_padded[3:len(node)] = node

                    table_nodes.append(node_padded)

    table_types = [[id, type_name] for type_name, id in types_unique.items()]

    return Dataset(
        steps=pl.DataFrame(table_steps, ['step_id', 'step_name']),
        types=pl.DataFrame(table_types, ['type_id', 'type_name']),
        frames=pl.DataFrame(table_frames, ['frame_id', 'step_id', 'frame_num']),
        nodes=pl.DataFrame(table_nodes, ['node_id', 'type_id', 'frame_id', 'val1', 'val2', 'val3', 'val4', 'val5', 'val6']),
    )

def to_dataset2(data: dict):
    table = pa.table(data)
    part = ds.partitioning(dictionaries=data, flavor='hive')
    ds.write_dataset(table, partitioning=part, base_dir='data/arrow', format="parquet")
    #ds.write_dataset(arr, 'data/arrow', format="parquet")

def save_table_as_parquet(table: pl.DataFrame, path: str):
    table.write_parquet(path)

def save_table_as_csv(table: pl.DataFrame, path: str):
    table.write_csv(path)

def save_table_as_sqlite(table: pl.DataFrame, path: str):
    conn = sqlite3.connect(path)

    with conn:
        sql = '''
            CREATE TABLE IF NOT EXISTS data(
                id integer PRIMARY KEY,
                step_name text,
                frame_num text,
                type_name text,
                val1 real,
                val2 real,
                val3 real,
                val4 real,
                val5 real,
                val6 real
            );
        '''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        for row in table:
            sql = '''
                INSERT INTO data(
                    step_name,
                    frame_num,
                    type_name,
                    val1,
                    val2,
                    val3,
                    val4,
                    val5,
                    val6
                ) VALUES (?,?,?,?,?,?,?,?,?)
            '''
            cur = conn.cursor()
            cur.execute(sql, row)
        conn.commit()

def save_as_compressed(data, path: str):
    json_data = json.dumps(data)
    encoded = json_data.encode('utf-8')
    compressed = gzip.compress(encoded)
    file = open(path, 'wb')
    file.write(compressed)
    file.close()

def save_as_pickle(data, path):
    file = open(path, 'wb')
    pickle.dump(data, file)
    file.close()

def save_table_as_arrow_table(table, path: str):
    table = from_dataframe(table)
    pq.write_table(table, path)

def save_table_as_arrow_dataset(table, path: str):
    table = from_dataframe(table)
    part = ds.partitioning(pa.schema([
        ('step_name', pa.large_string()),
        ('frame_num', pa.int32()),
    ]), flavor=None)

    ds.write_dataset(table, path, format='parquet', partitioning=part)


if __name__ == '__main__':
    data = read_data('data/data.json')
    table = to_table(data)
    #save_table_as_csv(table, 'data/data.csv')
    #save_table_as_parquet(table, 'data/data.parquet')
    #save_as_pickle(table, 'data/table.pickle')
    #save_as_pickle(data, 'data/data.pickle')
    #save_as_compressed(data, 'data/data.gz')
    #save_table_as_sqlite(table, 'data/data.sqlite')
    #save_table_as_arrow_table(table, 'data/arrow-table')
    save_table_as_arrow_dataset(table, 'data/arrow-dataset')

    #dataset = to_dataset(data)
    #dataset.to_parquet('data/polars')
