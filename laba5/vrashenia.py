import numpy as np
import math 
 
n = 3
A = np.random.randint(1, 10, size=(n, n))
def sym(a):
    sym_a = np.tril(a) + np.transpose(np.tril(a, -1))
    return sym_a
 
def Reform(a):
    if np.linalg.det(a) == 0 :
        return None
    row = []
    for i in range(1, n + 1):
        row = a[i - 1]
        max_index = np.argmax(row)
        summa = np.sum(row, dtype=np.float32) - row[max_index]
        a[i - 1][i - 1], row[max_index] = row[max_index], a[i - 1][i - 1]
    return A
 
A = Reform(A)
A_sym = sym(A)
print("Матрица:")
print(A_sym)
def tri_diag(a):
    t = np.identity(n)
 
    for i in range(2, n):
        for j in range(i + 1, n + 1):
            c = a[i - 2][i - 1]/(np.sqrt((a[i - 2][i - 1])**2 + (a[i - 2][j - 1])**2 ))
            s = -a[i - 2][j - 1]/(np.sqrt((a[i - 2][i - 1])**2 + (a[i - 2][j - 1])**2 ))
            t[i - 1][i - 1] = t[j - 1][j - 1] = c
            t[i - 1][j - 1] = s
            t[j - 1][i - 1] = -s
            matr = np.matmul(np.transpose(t), np.matmul(A_sym, t), dtype = np.float64)
    return matr

for m in range(10000):
    A = tri_diag(A_sym)
    A_sym = A
print(A)