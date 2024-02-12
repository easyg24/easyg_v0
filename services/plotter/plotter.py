import pandas as pd
import matplotlib.pyplot as plt

from models import Configurations


def get_data(file_path):
    df = pd.read_csv(file_path, sep=",", index_col=0)

    return df


def plot_data(data, configs):
    plt.title(configs.title)
    plt.xlabel(configs.xlabel)
    plt.ylabel(configs.ylabel)
    plt.grid(configs.grid)
    
    plt.plot(data)
    plt.scatter(data.index, data.y)
    
    plt.show()


def run():
    file_path = "../../tests/data/test.csv"
    data = get_data(file_path)
    plot_data(data, Configurations())


if __name__ == "__main__":
    run()