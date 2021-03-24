import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt


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
    reg = linear_model.LinearRegression()
    reg.fit(obj.height.reshape(-1, 1), obj.weight.reshape(-1, 1))
    w = [reg.coef_.tolist()[0][0], reg.intercept_.tolist()[0]]
    print('Coefficients: \n', w)
    plots(obj.x, obj.y, obj.names, w)

