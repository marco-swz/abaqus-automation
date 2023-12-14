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

def read_data(path: str) -> dict:
    file = open(path)
    data = json.load(file)
    file.close()
    return data

def to_table(data: dict) -> pl.DataFrame:
    table = [];
    for step_name, step in data.items():
        for frame_num, frame in step.items():
            print(step_name, frame_num)
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

class ParquetTable:
    @staticmethod
    def convert(in_path: str, out_path: str):
        data = read_data(in_path)
        table = to_table(data)
        table.write_parquet(out_path)

    @staticmethod
    def read_batch(path, steps, types, num_samples):
        table = pl.read_parquet(path)

        table.filter(
            pl.col('step_name').is_in(steps['step_name']) & 
            pl.col('val_type').is_in(types['type_name']) & 
            pl.col('frame_num').is_in(pl.col('frame_num').sample(num_samples, with_replacement=True))
        )

class ParquetDataset:
    @staticmethod
    def convert(in_path: str, out_dir: str):
        data = read_data(in_path)
        dataset = to_dataset(data)
        dataset.steps.write_parquet(out_dir+'/steps.parquet')
        dataset.frames.write_parquet(out_dir+'/frames.parquet')
        dataset.types.write_parquet(out_dir+'/types.parquet')
        dataset.nodes.write_parquet(out_dir+'/nodes.parquet')

    @staticmethod
    def read_batch(path, steps, types, num_frames):
        table_frames = pl.read_parquet(path+'/frames.parquet')\
            .filter(pl.col('step_id').is_in(steps['step_id']))\
            .sample(num_frames, with_replacement=True)

        samples = pl.read_parquet(path+'/nodes.parquet')\
            .filter(
                pl.col('type_id').is_in(types['type_id']) &
                pl.col('frame_id').is_in(table_frames['frame_id'])
            )
        print(samples.shape)

class CsvTable:
    @staticmethod
    def convert(in_path: str, out_path: str):
        data = read_data(in_path)
        table = to_table(data) 
        table.write_csv(out_path)

    @staticmethod
    def read_batch(path, steps, types, num_samples: int):
        table = pl.read_csv(path, dtypes={ 'frame_num': pl.Utf8 })

        samples = table\
            .filter(
                pl.col('step_name').is_in(steps['step_name']) & 
                pl.col('val_type').is_in(types['type_name']) &
                pl.col('frame_num').is_in(pl.col('frame_num').sample(num_samples, with_replacement=True))
            )
        print(samples.shape)

class SqliteTable:
    @staticmethod
    def convert(in_path: str, out_path: str):
        data = read_data(in_path)
        table = to_table(data) 
        conn = sqlite3.connect(out_path)

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

            for row in table.rows():
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

    @staticmethod
    def read_batch(path, steps: pl.DataFrame, types, num_frames: int):
        step_list = steps['step_name'].str.concat('","').to_list()[0]
        type_list = types['type_name'].str.concat('","').to_list()[0]

        conn = sqlite3.connect(path)
        with conn:
            # TODO(marco): Fix query
            sql = f'''
                select 
                    *
                from
                    data
                where
                    step_name in ("{step_list}")
                and type_name in ("{type_list}")
                and frame_num in (
                    select 
                        frame_num
                    from
                        data
                    where
                        step_name in ("{step_list}")
                        and type_name in ("{type_list}")
                    order by random() limit {num_frames}
                )
            '''
            cur = conn.cursor()
            cur.execute(sql)
            cur.fetchall()
            conn.commit()

def save_as_compressed(data, path: str):
    json_data = json.dumps(data)
    encoded = json_data.encode('utf-8')
    compressed = gzip.compress(encoded)
    file = open(path, 'wb')
    file.write(compressed)
    file.close()

class PickleDict:
    def convert(self, path: str):
        data = read_data(path)
        file = open(path, 'wb')
        pickle.dump(data, file)
        file.close()

    def read_batch(self, steps, types, frames):
        pass


class ArrowTable:
    def convert(self, path: str):
        data = read_data(path)
        table = to_table(data)
        table = from_dataframe(table)
        pq.write_table(table, path)

class ArrowDataset:
    def convert(self, path: str):
        data = read_data(path)
        table = to_table(data)
        table = from_dataframe(table)
        part = ds.partitioning(pa.schema([
            ('step_name', pa.large_string()),
            ('frame_num', pa.int32()),
        ]), flavor=None)

        ds.write_dataset(table, path, format='parquet', partitioning=part)

def read_batch(path: str, storage):
    data = read_data('data/data.json')
    dataset = to_dataset(data)


    steps = dataset.steps.sample(fraction=0.67)
    types = dataset.types.sample(fraction=0.67)
    storage.read_batch(path, steps, types, 10)


if __name__ == '__main__':
    #CsvTable.convert('data/data.json', 'data/table.csv')
    #read_batch('data/table.csv', CsvTable)

    #ParquetTable.convert('data/data.json', 'data/table.parquet')
    #read_batch('data/table.parquet', ParquetTable)

    #SqliteTable.convert('data/data.json', 'data/table.sqlite')
    #read_batch('data/table.sqlite', SqliteTable)

    ParquetDataset.convert('data/data.json', 'data/parquet')
    read_batch('data/parquet', ParquetDataset)

    #data = read_data('data/data.json')
    #table = to_table(data)
    #save_table_as_csv(table, 'data/data.csv')
    #save_table_as_parquet(table, 'data/data.parquet')
    #save_as_pickle(table, 'data/table.pickle')
    #save_as_pickle(data, 'data/data.pickle')
    #save_as_compressed(data, 'data/data.gz')
    #save_table_as_sqlite(table, 'data/data.sqlite')
    #save_table_as_arrow_table(table, 'data/arrow-table')
    #save_table_as_arrow_dataset(table, 'data/arrow-dataset')

    #dataset = to_dataset(data)
    #dataset.to_parquet('data/polars')
