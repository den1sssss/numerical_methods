#метод половинного деления(дихотомии)
from math import fabs
eps = 0.001
n = 20
 
def f(x):
    return((x-10)**3*(x+7)**4)

def pol_del(a, b):
    c = (a + b) / 2
    while(fabs(f(c)) > eps):
        for i in range(n):
            print(i)
            if(f(a) * f(c) < 0):
                b = c
            else:
                a = c
            c = (a + b) / 2
            i+=1
    print(c)    
    
a = 7.5
b=11.2
pol_del(a,b)
