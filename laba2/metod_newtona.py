from math import fabs
# import numpy as np
def f(x):
    return(x**5 + 2*x**4 - 5*x**3 + 8*x**2 - 7*x - 3)
# def f1_sekushie(x):
#     return()
# def f2_nb(x):
#     return(1)
# def f3_uprosh(x):
#     return()
def df(x):
    return(5*x**4 + 8*x**3 - 15*x**2 + 16*x - 7)
def newton():
    eps = 0.001
    x = -10
    while(fabs(f(x)) > eps):
        x = x - f(x)/df(x)
    print(x)
    x = 0
    while(fabs(f(x)) > eps):
        x = x - f(x)/df(x)
    print(x)
    x = 10
    while(fabs(f(x)) > eps):
        x = x - f(x)/df(x)
    print(x)

print("Newton:")
newton()