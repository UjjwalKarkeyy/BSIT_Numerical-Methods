import numpy as np

def simpson_three_eight_rule(f,a,b,n):
    if n % 3 != 0:
        return (print("n must be even for Simpson's 1/3 Rule"))
    
    h = (b - a) / n

    result = f(a) + f(b)

    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + (i * h))
        else:
            result += 3 * f(a + (i * h))
    return (3*h/8) * result

a, b = 0,2
n = 6
f = lambda x: (np.exp(-x**2)) / (1 + x**2)
print(simpson_three_eight_rule(f,a,b,n))