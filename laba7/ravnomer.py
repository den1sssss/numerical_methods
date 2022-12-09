import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations as comb

X = [1, 4, 7, 10, 13, 16]
Y = [1, -1, 3, 5, 14, 15]

def func1(k, y_values):
    coef = 0
    for j in range(k + 1):
          coef += -(-1 if (k - j) % 2 == 0 else 1) * Sochetanie(k, j) * y_values[j]
    coef /= np.math.factorial(k)
    return coef


def Sochetanie(n, k):
    return len(list(comb([0]*n, k)))


def Newton_1(x_values, y_values, h):
    def newton1(x):
        result = 0
        for k in range(len(x_values)):
            coef = 0
            if k == 0:
                coef = y_values[0]
            else:
                coef = func1(k, y_values)
            for j in range(k):
                coef *= (x - x_values[0]) / h - j
            result += coef
        return result
    return newton1

function1 = Newton_1(X, Y, X[1] - X[0])
new_X1 = np.arange(0, 7, 0.1)
function_values1 = [function1(i) for i in new_X1]

plt.plot(X[:3], Y[:3], linewidth=2, color='red')
plt.plot(new_X1, function_values1, linewidth=2, color='purple')
plt.grid()

print("N1(n)[0] =", function1(0))
print("N1(n)[8] =", function1(8))
print("N1(n)[17] =", function1(17))