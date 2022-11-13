import numpy as np

def zeidel(A, b, eps):
    n = len(A)
    x = np.zeros(n)

    while (np.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps):
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        x = x_new

    return x

# A = [[2,2,10],[10,1,1],[2,10,1]]
A = np.array([[2.0,2.0,10.0],[10.0,1.0,1.0],[2.0,10.0,1.0]])
# b = [14,12,13]
b = np.array([14.0,12.0,13.0])
eps = 0.01
zeidel(A,b,eps)