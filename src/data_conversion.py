import pyarrow as pa
import pyarrow.dataset as ds
import pyarrow.parquet as pq
import pyarrow.compute as pc
from pyarrow.interchange import from_dataframe
import time
import json
import polars as pl
import numpy as np
import gzip
import sqlite3
from dataclasses import dataclass

FRAME_REPEATS = 10

@dataclass
class Dataset:
    steps: ... 
    frames: ...
    types: ...
    nodes: ...

def read_json(path: str) -> dict:
    file = open(path)
    data = json.load(file)
    file.close()
    return data

def write_json(obj: dict, path: str):
    file = open(path, 'w')
    json.dump(obj, file)
    file.close()

def to_table(data: dict) -> pl.DataFrame:
    table = [];
    for step_name, step in data.items():
        for frame_num, frame in step.items():
            for frame_repeats in range(FRAME_REPEATS):
                frame_num_repeat = frame_num + str(frame_repeats)
                for val_type, nodes in frame.items():
                    for node in nodes:
                        node_padded = [np.NaN]*6
                        if isinstance(node, float):
                            node = [node]
                        node_padded[:len(node)] = node

                        row = [
                            step_name,
                            frame_num_repeat,
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
    node_id = -1
    frame_id = -1
    for step_id, step_name in enumerate(data.keys()):
        table_steps.append([step_id, step_name])
        step = data[step_name]

        for frame_num, types in step.items():
            for frame_repeats in range(FRAME_REPEATS):
                frame_num_repeat = frame_num + str(frame_repeats)
                frame_id += 1
                table_frames.append([frame_id, step_id, frame_num_repeat])

                for node_type, nodes in types.items():
                    type_id = types_unique.get(node_type)
                    if type_id is None:
                        types_id += 1
                        types_unique[node_type] = types_id
                        type_id = types_id

                    for node in nodes:
                        node_id += 1
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

class ParquetTable:
    name = 'Parquet single'

    @staticmethod
    def convert(in_path: str, out_path: str):
        data = read_json(in_path)
        table = to_table(data)
        table.write_parquet(out_path)

    @staticmethod
    def read_batch(path, steps, types):
        table = pl.read_parquet(path)

        samples = table.filter(
            pl.col('step_name').is_in(steps['step_name']) & 
            pl.col('val_type').is_in(types['type_name'])
        )

class ParquetDataset:
    name = "Parquet multiple"

    @staticmethod
    def convert(in_path: str, out_dir: str):
        data = read_json(in_path)
        dataset = to_dataset(data)
        dataset.steps.write_parquet(out_dir+'/steps.parquet')
        dataset.frames.write_parquet(out_dir+'/frames.parquet')
        dataset.types.write_parquet(out_dir+'/types.parquet')
        dataset.nodes.write_parquet(out_dir+'/nodes.parquet')

    @staticmethod
    def read_batch(path, steps, types):
        table_frames = pl.read_parquet(path+'/frames.parquet')\
            .filter(pl.col('step_id').is_in(steps['step_id']))

        samples = pl.read_parquet(path+'/nodes.parquet')\
            .filter(
                pl.col('type_id').is_in(types['type_id']) &
                pl.col('frame_id').is_in(table_frames['frame_id'])
            )

class CsvTable:
    name = 'CSV single'

    @staticmethod
    def convert(in_path: str, out_path: str):
        data = read_json(in_path)
        table = to_table(data) 
        table.write_csv(out_path)

    @staticmethod
    def read_batch(path, steps, types):
        table = pl.read_csv(path, dtypes={})

        samples = table\
            .filter(
                pl.col('step_name').is_in(steps['step_name']) & 
                pl.col('val_type').is_in(types['type_name'])
            )

class SqliteTable:
    name = 'Sqlite single'

    @staticmethod
    def convert(in_path: str, out_path: str):
        data = read_json(in_path)
        table = to_table(data) 
        conn = sqlite3.connect(out_path)

        with conn:
            sql = '''
                DROP TABLE IF EXISTS data;
            '''
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            
            sql = '''
                CREATE TABLE data(
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
    def read_batch(path, steps: pl.DataFrame, types):
        step_list = steps['step_name'].str.concat('","').to_list()[0]
        type_list = types['type_name'].str.concat('","').to_list()[0]

        conn = sqlite3.connect(path)
        with conn:
            sql = f'''
                select 
                    *
                from
                    data
                where
                    step_name in ("{step_list}")
                and type_name in ("{type_list}")
            '''
            cur = conn.cursor()
            cur.execute(sql)
            samples = cur.fetchall()
            conn.commit()

        samples = pl.DataFrame(np.array(samples))

class SqliteDataset:
    name = 'Sqlite multiple'

    @staticmethod
    def convert(in_path: str, out_path: str):
        data = read_json(in_path)
        dataset = to_dataset(data) 
        conn = sqlite3.connect(out_path)

        with conn:
            cur = conn.cursor()

            cur.execute('DROP TABLE IF EXISTS steps')
            cur.execute('DROP TABLE IF EXISTS types')
            cur.execute('DROP TABLE IF EXISTS frames')
            cur.execute('DROP TABLE IF EXISTS nodes')
            conn.commit()
            
            sql = '''
                CREATE TABLE steps(
                    step_id integer PRIMARY KEY,
                    step_name text
                );
            '''
            cur.execute(sql)

            sql = '''
                CREATE TABLE types(
                    type_id integer PRIMARY KEY,
                    type_name text
                );
            '''
            cur.execute(sql)

            sql = '''
                CREATE TABLE frames(
                    frame_id integer PRIMARY KEY,
                    step_id integer,
                    frame_num text
                );
            '''
            cur.execute(sql)

            sql = '''
                CREATE TABLE nodes(
                    node_id integer PRIMARY KEY,
                    frame_id integer,
                    type_id integer,
                    val1 real,
                    val2 real,
                    val3 real,
                    val4 real,
                    val5 real,
                    val6 real
                );
            '''
            cur.execute(sql)

            for step in dataset.steps.rows():
                sql = '''
                    INSERT INTO steps(
                        step_id,
                        step_name
                    ) VALUES (?,?)
                '''
                cur.execute(sql, step)

            for frame in dataset.frames.rows():
                sql = '''
                    INSERT INTO frames(
                        frame_id,
                        step_id,
                        frame_num
                    ) VALUES (?,?,?)
                '''
                cur.execute(sql, frame)

            for types in dataset.types.rows():
                sql = '''
                    INSERT INTO types(
                        type_id,
                        type_name
                    ) VALUES (?,?)
                '''
                cur.execute(sql, types)

            for node in dataset.nodes.rows():
                sql = '''
                    INSERT INTO nodes(
                        node_id,
                        type_id,
                        frame_id,
                        val1,
                        val2,
                        val3,
                        val4,
                        val5,
                        val6
                    ) VALUES (?,?,?,?,?,?,?,?,?)
                '''
                cur.execute(sql, node)

            conn.commit()

    @staticmethod
    def read_batch(path, steps: pl.DataFrame, types):
        step_list = steps['step_id'].str.concat('","').to_list()[0]
        type_list = types['type_id'].str.concat('","').to_list()[0]

        conn = sqlite3.connect(path)
        with conn:
            sql = f'''
                select 
                    *
                from
                    nodes
                where
                    frame_id in (
                        select
                            frame_id 
                        from
                            frames
                        where step_id in ("{step_list}")
                    )
                and type_id in ("{type_list}")
            '''
            cur = conn.cursor()
            cur.execute(sql)
            samples = cur.fetchall()
            conn.commit()

        samples = pl.DataFrame(np.array(samples))

def save_as_compressed(data, path: str):
    json_data = json.dumps(data)
    encoded = json_data.encode('utf-8')
    compressed = gzip.compress(encoded)
    file = open(path, 'wb')
    file.write(compressed)
    file.close()

class ArrowTable:
    name = "Arrow single"

    @staticmethod
    def convert(in_path: str, out_path: str):
        data = read_json(in_path)
        table = to_table(data)
        table = from_dataframe(table)
        pq.write_table(table, out_path)

    @staticmethod
    def read_batch(path, steps, types):
        table = pq.read_table(path)
        samples = table\
            .filter(
                pc.field('step_name').isin(steps['step_name']) &
                pc.field('val_type').isin(types['type_name'])
            )


class ArrowTablePart:
    name = "Arrow partitioned"

    @staticmethod
    def convert(in_path: str, out_path: str):
        data = read_json(in_path)
        table = to_table(data)
        table = from_dataframe(table)
        part = ds.partitioning(pa.schema([
            ('step_name', pa.large_string()),
            ('val_type', pa.large_string()),
        ]), flavor='hive')

        ds.write_dataset(table, out_path, format='parquet', partitioning=part, existing_data_behavior='overwrite_or_ignore')

    @staticmethod
    def read_batch(path, steps, types):
        part = ds.partitioning(pa.schema([
            ('step_name', pa.large_string()),
            ('val_type', pa.large_string()),
        ]), flavor='hive')
        dataset = ds.dataset(path, partitioning=part)
        samples = dataset.filter(
            pc.field('step_name').isin(steps['step_name']) &
            pc.field('val_type').isin(types['type_name'])
        )

        samples = pl.from_arrow(samples.to_table())

def read_batch(input_file:str, path: str, storage):
    data = read_json(input_file)
    dataset = to_dataset(data)
    num_reads = 10
    seeds = np.arange(0, num_reads)
    timings = np.zeros(num_reads)

    for i, seed in enumerate(seeds):
        steps = dataset.steps.sample(fraction=0.67, seed=seed)
        types = dataset.types.sample(fraction=0.67, seed=seed)
        start = time.time()
        storage.read_batch(path, steps, types)
        timings[i] = time.time() - start

    print(f'Benchmark done for `{storage.name}`')
    print(f'\tMean: {timings.mean()}')
    print(f'\tStd: {timings.std()}')

    stats = dict(
        storage_name=storage.name,
        read_durations_s=list(timings),
        frame_repeats=FRAME_REPEATS,
    )
    write_json(stats, f'benchmarks/{storage.name.lower().replace(" ", "-")}-{FRAME_REPEATS}.json')


if __name__ == '__main__':
    input_file = 'data/data.json'
    CsvTable.convert(input_file, 'data/table.csv')
    read_batch(input_file, 'data/table.csv', CsvTable)

    ParquetTable.convert(input_file, 'data/table.parquet')
    read_batch(input_file, 'data/table.parquet', ParquetTable)

    SqliteTable.convert(input_file, 'data/table.sqlite')
    read_batch(input_file, 'data/table.sqlite', SqliteTable)

    SqliteDataset.convert(input_file, 'data/dataset.sqlite')
    read_batch(input_file, 'data/dataset.sqlite', SqliteDataset)

    ParquetDataset.convert(input_file, 'data/parquet')
    read_batch(input_file, 'data/parquet', ParquetDataset)

    ArrowTablePart.convert(input_file, 'data/arrow-table-part')
    read_batch(input_file, 'data/arrow-table-part', ArrowTablePart)

    ArrowTable.convert(input_file, 'data/arrow-table')
    read_batch(input_file, 'data/arrow-table', ArrowTable)
