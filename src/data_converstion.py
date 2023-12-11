import json
import polars as pl
import numpy as np

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

def save_table_as_parquet(table: list):
    df = pl.DataFrame(table)
    df.write_parquet('data/data.parquet')

def save_table_as_csv(table: list):
    df = pl.DataFrame(table)
    df.write_csv('data/data.csv')

def save_as_compressed(data, path):
    # TODO(marco)
    pass

def save_as_pickle(data, path):
    # TODO(marco)
    pass

if __name__ == '__main__':
    data = read_data('data/data.json')
    table = to_table(data)
    save_table_as_csv(table)

