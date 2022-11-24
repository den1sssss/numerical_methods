import numpy as np
import math
import matplotlib.pyplot as plt
# a = -1.5
# b = 1.5

def f(x):
    return math.tan(x)+1

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

z = []
lag_pol = create_Lagrange_polynomial(x_values, y_values)
for i in range(16):
    z.append(lag_pol(x_values[i]))
# plt.plot(z,lag_pol)
plt.plot(x_values,y_values)

lag_pol_values = [lag_pol(x_values[i]) for i in range(len(x_values))]
# plt.plot(x_values,create_Lagrange_polynomial(x_values,y_values))#?
plt.plot(x_values,lag_pol_values)
plt.show()


#### пункт Б

def find_Lag_1(x, x_values, y_values):
    i = 0
    while x_values[i] < x:
        index_1 = x_values[i]
        index_2 = x_values[i + 1]
        value_1 = y_values[i]
        value_2 = y_values[i + 1]
        i += 1
    lag_1_values = [index_1, index_2]
    polynomial_1 = create_basic_polynomial(lag_1_values, 0)
    polynomial_2 = create_basic_polynomial(lag_1_values, 1)
    return polynomial_1(x) * value_1 + polynomial_2(x) * value_2

print("Value in 1.3:")
print(find_Lag_1(1.3,x_values,y_values))


#### пункт В

def find_Lag_2(x, x_values, y_values):
    i = 0
    while x_values[i] < x:
        index_1 = x_values[i - 1]
        index_2 = x_values[i]
        value_1 = y_values[i - 1]
        value_2 = y_values[i]
        index_3 = x_values[i + 1]
        index_4 = x_values[i + 2]
        value_3 = y_values[i + 1]
        value_4 = y_values[i + 2]
        i += 1
    lag_2_values_1 = [index_1, index_2, index_3]
    lag_2_values_2 = [index_2, index_3, index_4]
    polynomial_1_1 = create_basic_polynomial(lag_2_values_1, 0)
    polynomial_2_1 = create_basic_polynomial(lag_2_values_1, 1)
    polynomial_3_1 = create_basic_polynomial(lag_2_values_1, 2)
    polynomial_1_2 = create_basic_polynomial(lag_2_values_2, 0)
    polynomial_2_2 = create_basic_polynomial(lag_2_values_2, 1)
    polynomial_3_2 = create_basic_polynomial(lag_2_values_2, 2)
    L_1 = polynomial_1_1(x) * value_1 + polynomial_2_1(x) * value_2 + polynomial_3_1(x) * value_3
    L_2 = polynomial_1_2(x) * value_2 + polynomial_2_2(x) * value_3 + polynomial_3_2(x) * value_4
    return (L_1 + L_2) / 2

print("Value for v) в точке 1:")
print(find_Lag_2(1,x_values,y_values))
# print(lag_pol(4))
# for x in x_values:
#     print("x = {:.4f}\t y = {:4f}".format(x,lag_pol(x)))