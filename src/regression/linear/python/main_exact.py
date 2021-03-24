from classes import *
import numpy as np


if __name__ == '__main__':
    data_path = "../../../../data/weight-height.csv"
    obj = mice(data_path)

    # exact
    # https://cutt.ly/6xUiR3B
    M = np.array([[np.dot(obj.x, obj.x), np.sum(obj.x)], [np.sum(obj.x), len(obj.x)]])
    B = np.array([np.dot(obj.x, obj.y), np.sum(obj.y)])
    w = np.linalg.solve(M, B)
    print(w)
    plots(obj.x, obj.y, obj.names, w)

