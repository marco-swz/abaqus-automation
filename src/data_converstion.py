import json
import polars as pl
import numpy as np
import pickle
import gzip
import sqlite3

def read_data(path: str) -> dict:
    file = open(path)
    data = json.load(file)
    file.close()
    return data

def to_table(data: dict):
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
    return table

def save_table_as_parquet(table: list, path: str):
    df = pl.DataFrame(table)
    df.write_parquet(path)

def save_table_as_csv(table: list, path: str):
    df = pl.DataFrame(table)
    df.write_csv(path)

def save_table_as_sqlite(table: list, path: str):
    conn = sqlite3.connect(path)

    with conn:
        sql = '''
            CREATE TABLE IF NOT EXISTS data(
                id integer PRIMARY KEY,
                step text,
                frame text,
                type text,
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
                    step,
                    frame,
                    type,
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

if __name__ == '__main__':
    data = read_data('data/data.json')
    table = to_table(data)
    #save_table_as_csv(table, 'data/data.csv')
    #save_table_as_parquet(table, 'data/data.parquet')
    #save_as_pickle(table, 'data/table.pickle')
    #save_as_pickle(data, 'data/data.pickle')
    #save_as_compressed(data, 'data/data.gz')
    save_table_as_sqlite(table, 'data/data.sqlite')

