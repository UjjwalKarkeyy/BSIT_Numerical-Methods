import math

f = lambda x: math.sin(x) * ((x**2)/5) + x

def newtonMethod(xi, first_derv, second_derv):
    for i in range(max_itr):
        x_new = xi - (first_derv(xi)/second_derv(xi))
        if ((tol-0.5) <= first_derv(xi) <= (tol+0.5)):
            return x_new
        print(f"x_new: {x_new}\t\tfirst_derv: {first_derv(x_new)}")
        xi = x_new
tol = 0
max_itr = 1000
xi = 0
first_derv = lambda xi: math.cos(xi) - ((2*xi)/5) + 1
second_derv = lambda xi: -(math.sin(xi)) - 2/5
newtonMethod(xi,first_derv, second_derv)