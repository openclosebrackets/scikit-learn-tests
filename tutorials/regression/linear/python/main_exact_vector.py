from classes import *
import numpy as np


if __name__ == '__main__':
    data_path = "../../../../data/weight-height.csv"
    obj = mice(data_path)

    xbar = np.average(obj.x)
    ybar = np.average(obj.y)
    newX = obj.x - xbar
    newY = obj.y - ybar

    m = np.dot(newX, newY) / np.dot(newX, newX)
    b = ybar - m * xbar
    w = [m, b]
    plots(obj.x, obj.y, obj.names, w)

