import numpy as np
import copy

def unfolding_method(A):

    def get_lambdas(coefficients):

        def get_root(coefs):

            def f(x, a=coefs):
                res = 0
                for k, coef in enumerate(a[::-1]):
                    res += coef * x ** k
                return res

            def f1(x, a=coefs):
                res = 0
                for k, coef in enumerate(a[::-1]):
                    if k != 0:
                        res += coef * k * x ** (k-1)
                return res

            N_iter = 300
            eps = 10e-10
            c = 0.6
            x_prev = 0
            x_next = x_prev - c * f(x_prev) / f1(x_prev)

            while abs(x_next - x_prev) > eps and N_iter > 0:
                N_iter -= 1
                x_prev = x_next
                x_next = x_prev - c * f(x_prev) / f1(x_prev)

            return x_next

        def extract_root(coefs, x):
            eps = 10e-6
            res = []
            c_prev = 0
            for coef in coefs[:-1]:
                c_new = coef + x * c_prev
                res.append(c_new)
                c_prev = c_new

            remnant = c_prev * x + coefs[-1]
            if abs(remnant) > eps:
                return None
            else:
                return res

        c = coefficients.copy()
        lambdas = []

        n = len(c)
        for i in range(n):
            lam_next = get_root(c)
            lambdas.append(lam_next)

            c = extract_root(c, lam_next)
            if len(c) == 1:
                break

        return lambdas

    def get_vectors(M, lams):

        vects=[]
        for lam in lams:
            B = copy.deepcopy(M)
            for i in range(n):
                B[i][i] -= lam

            X = [1, -B[0][0]/B[0][1]]
            vects.append(X)

        return vects


    n = len(A)
    char_eq = [1, -A[0][0] -A[1][1], A[0][0] * A[1][1] - A[0][1] * A[1][0]]
    lambdas = get_lambdas(char_eq)
    vectors = get_vectors(A, lambdas)

    res = {}
    for i, lam in enumerate(lambdas):
        res[lam] = vectors[i]

    return res


C = [[2, 1],
     [1, 3]]

print(unfolding_method(C))
