import pandas as pd
import matplotlib.pyplot as plt


def get_data(file_path):
    df = pd.read_csv(file_path)
    
    return df


def plot_data(data):
    plt.plot(data)
    plt.show()


def run():
    file_path = "../../tests/data/test.csv"
    data = get_data(file_path)
    plot_data(data)


if __name__ == "__main__":
    run()