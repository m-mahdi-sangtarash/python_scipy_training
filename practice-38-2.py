from scipy.integrate import quad
import math as m

def f(x):
    return x * (m.e) ** (2 * x)


a = 0
b = 1
s = quad(f, a, b)
print(s)