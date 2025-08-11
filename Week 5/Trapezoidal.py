import math

def func(x):
    return math.exp(-x * -x)

def trapezoid(n, lower_bound, h, result):
    for i in range(1,n):
        result += 2 * func(lower_bound + (i * h))

    return h/2 * result

lower_bound = 1
upper_bound = 5
n = 8
h = (upper_bound - lower_bound) / n
result = func(lower_bound) + func(upper_bound)

print(trapezoid(n, lower_bound, h, result))
