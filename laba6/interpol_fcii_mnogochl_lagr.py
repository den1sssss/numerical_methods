import numpy as np
import math
import matplotlib.pyplot as plt
# a = -1.5
# b = 1.5

def f(x):
    return math.tan(x)+1


# import numpy as np
# # import matplotlib as plt
# import random

# x  = [50,60]
# a = 0
# while a < 13 :
#     random_number = random.uniform(0, 10) + 50
#     while random_number in x :
#         random_number = random.uniform(0, 10) + 50
#     x.append(random_number)
#     a = a + 1
#     x.sort()
# print(x)



# for k in range(len(x)):
#     y=np.sin(x)*(0.25)+100
 
# def poly(x, y, t):
#     z = 0
#     for i in phi():
#         c1 = 1
#         c2 = 1
#         for j in range(len(x)):
#             if i == j:
#                 c1 = c1 * 1
#                 c2 = c2 * 1
#             else:
#                 c1 = c1 * (t - x[j])
#                 c2 = c2 * (x[i] - x[j])
#         z = z + y[i] * c1 / c2
#     return z


# xnew = np.linspace(np.min(x), np.max(x), 100)
# ynew = [poly(x, y, j) for j in xnew]
# # plt.plot(x,y)
# # plt.plot(x,y,'o',xnew,ynew)
# # plt.grid(True)
# # plt.show()


def create_basic_polynomial(x_values, i):
    def basic_polynomial(x):
        divider = 1 #1
        result = 1
        for j in range(len(x_values)):
            if j != i:
                result *= (x-x_values[j])
                divider *= (x_values[i]-x_values[j])
        return result/divider
    return basic_polynomial


def create_Lagrange_polynomial(x_values, y_values):
    basic_polynomials = []
    for i in range(len(x_values)):
        basic_polynomials.append(create_basic_polynomial(x_values, i))

    def lagrange_polynomial(x):
        result = 0
        for i in range(len(y_values)):
            result += y_values[i]*basic_polynomials[i](x)
        return result
    return lagrange_polynomial


# x_values = [0, 2, 3, 5]
# y_values = [0, 1, 3, 2]
x_values = []
y_values = [] 
x0 = -1.5
for i in range(16):
    x_values.append(x0)
    x0+=0.2


print("ARRAY X:")
for i in range(len(x_values)):
    print('%.1f' % x_values[i])


print("ARRAY F(X)")
for i in range(16):
    y_values.append(f(x_values[i]))



for i in range(len(y_values)):
    print('%.5f' % y_values[i])


lag_pol = create_Lagrange_polynomial(x_values, y_values)

z = np.arange(-10, 10.01, 0.01)
plt.plot(z,lag_pol)
plt.show()
# print(lag_pol(4))
# for x in x_values:
#     print("x = {:.4f}\t y = {:4f}".format(x,lag_pol(x)))