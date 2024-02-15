from io import BytesIO

import pandas as pd
import matplotlib.pyplot as plt

from .models import Configurations

# import matplotlib
# matplotlib.use("agg")


def get_data(rawData: bytes):
    df = pd.read_csv(rawData, sep=",", index_col=0)
    return df

def build_configs(configs):
    plt.title(configs.title)
    plt.xlabel(configs.xlabel)
    plt.ylabel(configs.ylabel)
    plt.grid(configs.grid)
    

def build_plot(data):
    plt.plot(data)
    plt.scatter(data.index, data.y)


def build_graph(file, configs):
    fig = plt.figure()

    if not configs:
        configs = Configurations()
    
    build_configs(configs=configs)

    if file:
        data = get_data(file.file)
        build_plot(data=data)

    buffer = BytesIO()
    fig.savefig(buffer, format="png")

    return buffer.getvalue()
