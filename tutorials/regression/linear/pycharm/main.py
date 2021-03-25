import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from kaggle.api.kaggle_api_extended import KaggleApi



class database():
    def __init__(self, path):
        self.path = path
        self.data = None
        self.read_data_csv()

    def read_data_csv(self):
        self.data = pd.read_csv(self.path)
        print()


class mice(database):
    def __init__(self, path):
        super().__init__(path)
        self.height = self.data["Height"].to_numpy()
        self.weight = self.data["Weight"].to_numpy()
        self.x = self.height
        self.y = self.weight
        self.names = ["Height", "Weight"]


def plots(x, y, names, w):
    plt.scatter(x, y, s=1)
    plt.plot(x, x * w[0] + w[1])
    plt.xlabel(names[0])
    plt.ylabel(names[1])
    plt.show()


if __name__ == '__main__':
    data_path = "../../../../data/weight-height.csv"
    obj = mice(data_path)

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files('mustafaali96/weight-height', path='./', unzip=True)

    # exact
    # https://cutt.ly/6xUiR3B
    #M = np.array([[np.dot(obj.x, obj.x), np.sum(obj.x)], [np.sum(obj.x), len(obj.x)]])
    #B = np.array([np.dot(obj.x, obj.y), np.sum(obj.y)])
    #w = np.linalg.solve(M, B)
    #print(w)
    #plots(obj.x, obj.y, obj.names, w)
