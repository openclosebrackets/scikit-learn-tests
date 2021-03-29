from classes import *
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
import numpy as np

def error(ypred, ytarg):
    return 100 - 100 * np.dot(ypred, ytarg) / np.dot(ytarg, ytarg)
 

if __name__ == '__main__':
    boston_dataset = load_boston()
    y = boston_dataset.target
    x = boston_dataset.data[:, 12]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=25)

    xbar = np.average(x_train)
    ybar = np.average(y_train)
    newX = x_train - xbar
    newY = y_train - ybar

    las = [i for i in range(0, 20)]

    for la in las:
        m = np.dot(newX, newY) / (np.dot(newX, newX) + la)
        b = ybar - m * xbar
        w = [m, b]

        print(f"lamda = {la}")
        print(f"Target error : {error(x_train * w[0] + w[1], y_train):.3f} %")
        print(f"Test error : {error(x_test * w[0] + w[1], y_test):.3f} %")

        # names = ["Price", "LSTAT"]
        # plots(x, y, names, w)
        # plt.show()

