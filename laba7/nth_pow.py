import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations as comb

X = [1, 4, 7, 10, 13, 16]
Y = [1, -1, 3, 5, 14, 15]

def func2(k, y_values):
    coef = 0
    for j in range(k, len(y_values)):
          coef += (-1 if j % 2 == 0 else 1) * Sochetanie(len(y_values) - k - 1, len(y_values) - j - 1) * y_values[j]
    coef /= np.math.factorial(len(y_values) - k - 1)
    return coef


def Sochetanie(n, k):
    return len(list(comb([0]*n, k)))


def Newton_2(x_values, y_values, h):
    def newton2(x):
        result = 0
        for k in range(len(x_values) - 1, -1, -1):
            coef = 0
            if k == len(x_values) - 1:
                coef = y_values[k]
            else:
                coef = func2(k, y_values)
            for j in range(len(x_values) - 1, k, -1):
                coef *= ((x - x_values[-1]) / h + (len(x_values) - 1 - j))
            result += coef
        return result
    return newton2

function2 = Newton_2(X, Y, X[1] - X[0])
new_X2 = np.arange(10, 17, 0.1)
function_values2 = [function2(i) for i in new_X2]

plt.plot(X[3:], Y[3:], linewidth=2, color='red')
plt.plot(new_X2, function_values2, linewidth=2, color='blue')
plt.grid()

print("N2(n)[0] =", function2(0))
print("N2(n)[8] =", function2(8))
print("N2(n)[17] =", function2(17))