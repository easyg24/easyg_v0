from io import BytesIO

import PIL.Image as Image
import pandas as pd
import matplotlib.pyplot as plt

from models import Configurations


def get_data(file_path):
    df = pd.read_csv(file_path, sep=",", index_col=0)

    return df


def plot_data(data, configs):
    fig = plt.figure()
    
    plt.title(configs.title)
    plt.xlabel(configs.xlabel)
    plt.ylabel(configs.ylabel)
    plt.grid(configs.grid)
    
    plt.plot(data)
    plt.scatter(data.index, data.y)

    plt.show()

    buffer = BytesIO()
    fig.savefig(buffer, format="png")

    return buffer.getvalue()


def run():
    file_path = "../../tests/data/test.csv"
    data = get_data(file_path)
    response = plot_data(data, Configurations())
    
    image = Image.open(BytesIO(response))
    image.save('./tmp/test.png')


if __name__ == "__main__":
    run()