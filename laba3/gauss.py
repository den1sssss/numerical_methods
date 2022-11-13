import numpy as np 

def gauss(a, b):      
    m, n = a.shape 
    l = np.zeros((n,n))
    for i in range(n):
        if (a[i][i] == 0):
            print("no answer")
    for k in range(n - 1):         
        for i in range(k + 1, n):     
            l[i][k] = a[i][k] / a[k][k]          
            for j in range(m):          
                a[i][j] -= l[i][k] * a[k][j]
            b[i] = b[i] - l[i][k] * b[k]
    print("После:",a)
    print(b)
    x = np.zeros(n)                                              
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]  
    for i in range(n - 2, -1, -1):           
        for j in range(i + 1, n):
            b[i] -= a[i][j] * x[j]              
        x[i] = b[i] / a[i][i]
    for i in range(n):
        print("x" + str(i + 1) + " = ", x[i])
#---------
a = np.array([[2.0, 1.0, 4.0], 
    [3, 2, 1], 
    [1, 3, 3]])
b = np.array([16, 10, 16])
print("A:",a)
print("B:",b)                                                                        
gauss(a, b)         