import matplotlib.pyplot as plt
import os
import polars as pl
import numpy as np

def plot_sizes():
    data = pl.DataFrame(dict(
        name = [
            'CSV single', 
            'Parquet single',
            'Arrow single',
            'Sqlite single',
            'Parquet multiple',
            'Sqlite multiple',
            'Arrow partitioned',
        ],
        size = [
            429616239,
            24814550,
            16602118,
            339210240,
            29420000,
            140144640,
            39744000,
        ],
    ))

    data = data.sort(pl.col('size'))

    plt.barh(data['name'], data['size'])
    plt.title('Storage Size Comparison')
    plt.xlabel('Storage size [bytes]')
    plt.tight_layout()
    plt.show()

def plot_times():
    data = []
    for path in os.listdir('benchmarks'):
        data.append(pl.read_json('benchmarks/'+path))
    data = pl.concat(data)
    means = np.stack(data['read_durations_s'].to_numpy()).mean(1)
    #medians = data['read_durations_s'].to_numpy().median()
    stds = np.stack(data['read_durations_s'].to_numpy()).std(1)

    data = data.with_columns(means=pl.lit(means))
    data = data.with_columns(stds=pl.lit(stds))
    data = data.sort(pl.col('means'))

    plt.boxplot(data['read_durations_s'][:-2], vert=False, labels=data['storage_name'][:-2])
    plt.title('Read Time Comparison')
    plt.xlabel('Read Time [s]')
    plt.tight_layout()
    plt.show()



if __name__ == '__main__':
    plot_sizes()
    #plot_times()
