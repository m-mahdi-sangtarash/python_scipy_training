from scipy.integrate import quad
import math as m

def f(x):
    return (m.cos(x))**2 * m.sin(x)

a = 0
b = m.pi / 2
s = quad(f, a, b)
print(s)