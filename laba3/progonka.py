import numpy as np

A = np.array([[5,3,0,0],[3,6,1,0],[0,1,4,-2],[0,0,1,-3]])
B = np.array([8,10,3,-2])
def progonka(a,b):
    n = len(a)
    x = np.zeros(n)
    v=np.zeros(n)
    u = np.zeros(n)
    v[0]=a[0][1]/(-a[0][0])
    u[0] = (-b[0])/(-a[0][0])
    for i in range(1,n-1):
        v[i]=a[i][i+1]/(-a[i][i] - a[i][i-1]*v[i-1])
        u[i] = (a[i][i-1]*u[i-1]-b[i])/(-a[i][i] - a[i][i-1]*v[i-1])
    v[n-1]=0
    u[n-1]=(a[n-1][n-2]*u[n-2]-b[n-1])/(-a[n-1][n-1]-a[n-1][n-2]*v[n-2])

    x[n-1]=u[n-1]
    for i in range(n-1,0,-1):
        x[i-1]=v[i-1]*x[i]+u[i-1]
    return x
X = progonka(A,B)
print(X)