#метод простой итерации
import numpy as np
def deff(x):
    return(a/x + x)/2

eps = 0.01
N=20
x=np.zeros(N)
x[0]=7.5
x[1]=11.2
a = 4
n=1
while abs((x[n+1]-x[n])/(1-(x[n+1]-x[n])/(x[n]-x[n-1])))>eps:
    x[n+1]=deff(x[n])
    n+=1
    print("step",n)
print(x[n])