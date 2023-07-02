from scipy.integrate import quad
import math as m

def f(x):
    return m.log(x) / x

a = 2
b = 3
s = quad(f, a, b)
print(s)