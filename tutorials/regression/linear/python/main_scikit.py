from classes import *
from sklearn import linear_model

if __name__ == '__main__':
    data_path = "../../../../data/weight-height.csv"
    obj = mice(data_path)
    reg = linear_model.LinearRegression()
    reg.fit(obj.height.reshape(-1, 1), obj.weight.reshape(-1, 1))
    w = [reg.coef_.tolist()[0][0], reg.intercept_.tolist()[0]]
    print('Coefficients: \n', w)
    plots(obj.x, obj.y, obj.names, w)

