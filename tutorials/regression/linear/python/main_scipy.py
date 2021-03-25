from classes import *
from scipy.optimize import least_squares

def fun_lsm(w, height, weight):
    return weight - height * w[0] - w[1]

 
if __name__ == '__main__':
    data_path = "../../../../data/weight-height.csv"
    obj = mice(data_path)

    x0 = [0.1, 0.1]
    res = least_squares(fun_lsm, x0, args=(obj.height, obj.weight))
    plots(obj.x, obj.y, obj.names, res.x)
