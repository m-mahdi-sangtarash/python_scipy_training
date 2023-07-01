from scipy.optimize import minimize
import math as m


def f(x):
    return x + m.e ** x


mymin = minimize(f, 0, method="BFGS")
print(mymin)
