import numpy as np
import math

A=np.array([[1,2,3],[4,3,1],[3,4,6]])
eps = 0.1

def iter(A,eps):
    x0=np.ones(len(A))
    x1=A.dot(x0)
    lamb0=x1[0]/x0[0]

    x2 = A.dot(x1)
    lamb1=x2[0]/x1[0]

    while(abs(lamb1 - lamb0) > eps):
        xk=A.dot(x2)
        lamb0=xk[0]/x2[0]

        xk1=A.dot(xk)
        lamb1=xk1[0]/xk[0]

        x2 = xk1.copy()
    print("Значения:")
    print(lamb0)
    print("Векторы:")
    print(xk1)
iter(A,eps)