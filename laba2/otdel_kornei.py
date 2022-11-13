from math import fabs
import numpy as np

def f1(a):
    print("Теорема 1:")
    res = 0
    for i in range(len(a) - 1):
        res+=1
    print("Кол-во корней равно ",res)
def f2(a):
    print("Теорема 2:")
    if(len(a)%2 == 0):
        print("Уравнение имеет по крайней мере один действительный корень")
def f3(a):
    print("Теорема 3:")
    A = 0
    B = 0
    for i in range(1,len(a)):
        if(abs(a[i]) > A):
            A = abs(a[i])
    for i in range(len(a)-1):
        if(abs(a[i]) > B):
            B = abs(a[i])
    # print(A)
    # print(B)
    r = 1/(1+B/abs(a[len(a) - 1]))
    R = 1 + A/abs(a[0])
    print("left side(по модулю) = ",r)
    print("right side(по модулю) = ",R)
    return(R)

def f4(a):
    print("Теорема 4:")
    # a.reverse()
    for i in range(len(a)):
        if(a[i]<0):
            break
    C = 0
    iter = 0
    for i in range(len(a)):
        if(a[i] < C):
            C = a[i]
            iter = i
    C*=-1
    R = 1+pow(C/a[0],1/(len(a) - iter))
    print ("Верхняя граница = ",R)
    return(R)
def f5(a,R):
    print("Теорема 5:")
    a.reverse()
    # print(a)
    for i in range(0,len(a)):
        a[i]*=-1
    # print(a)
    C = 0
    iter = 0
    for i in range(len(a)):
        if(a[i] < C):
            C = a[i]
            iter = i
    C*=-1
    R1 = 1 + pow(C/a[0],1/(len(a) - 1 - iter))
    print(R1)
    print(1/R1, " < x(+) <= ",R)
    return(-R1)
def f6(a,R3):
    a.reverse()
    print("Для отрицательных корней:")
    # print(a)
    C = 0
    iter = 0
    for i in range(len(a)):
        if(a[i] < C):
            C = a[i]
            iter = i
    C*=-1
    R2 = 1 + pow(C/a[len(a)-1],1/(len(a) - 1 - iter + 1))
    # print(R2)
    print(-R2, " < x(-) <= ", 1/R3)
def f(x):
    return(x**5 + 2*x**4 - 5*x**3 + 8*x**2 - 7*x - 3)
a = [1,2,-5,8,-7,-3]
print(a)
f1(a)
f2(a)
R = f3(a)
R = f4(a)
R3 = f5(a,R)
f6(a,R3)