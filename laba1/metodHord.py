# Метод хорд
import numpy as np

eps = 0.01
N=20
x=np.zeros(N)
x[0]=7.5
x[1]=11.2
def f(x):
    return((x-10)**3*(x+7)**4)

n = 1
while((abs(x[n+1]-x[n])> eps and len(x)>n+2)):
    x[n+1] = x[n] - f(x[n])*(x[n-1]-x[n])/(f(x[n-1]) - f(x[n]))
    n+=1
print(x[n])