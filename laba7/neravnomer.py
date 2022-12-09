import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations as comb

X = [1, 4, 7, 10, 13, 16]
Y = [1, -1, 3, 5, 14, 15]

def func(values, res):
    if len(values) == 2:
        for i in range(len(X)):
            if X[i] == values[1]:
               res += Y[i]
            if X[i] == values[0]:
                res -= Y[i]
        res /= values[1] - values[0]
    else:
        res = (func(values[1:], res) - func(values[:-1], res)) / (values[len(values) - 1] - values[0])
    return res

def Global_newton(x_values, y_values):
    def global_newton(x):
        result = 0
        for i in range(len(x_values)):
            coef = 0
            if i == 0:
                coef = y_values[i]
            elif i == 1:
                coef = (y_values[1]- y_values[0]) / (x_values[1] - x_values[0])
            else:
                coef = func(x_values[0:i + 1], 0)
            for j in range(i):
                coef *= (x - x_values[j])
            result += coef
        return result

    return global_newton

function = Global_newton(X, Y)
new_X = np.arange(0, 17, 0.1)
function_values = [function(new_X[i]) for i in range(len(new_X))]

plt.plot(X, Y, linewidth=2, color='red')
plt.plot(new_X, function_values, linewidth=2, color='green')
plt.grid()

print("N(n)[0] =", function(0),"\nN(n)[8] =", function(8), "\nN(n)[17] =", function(17))
