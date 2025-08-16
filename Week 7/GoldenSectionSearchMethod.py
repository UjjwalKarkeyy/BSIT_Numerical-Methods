import math

f = lambda x: math.sin(x) * ((x-2)**2) + 4

def golden_search(f, xl,xu,tol,max_itr):
    for i in range(max_itr):
        d = ((math.sqrt(5) - 1)/2)*(xu-xl)
        x1 = xl + d
        x2 = xu - d
        if(f(x1) > f(x2)):
            xl = x2
        else:
            xu = x1
            
        if abs(xu-xl)<tol:
            break
        
    x_max = (xl + xu)/2
    return x_max, f(x_max)

xl = 0 
xu = 2
tol = 0.000011
max_itr = 1000
x_max, f_max = golden_search(f,xl,xu,tol,max_itr)
print(f"Max:{x_max:.5f}\nFunc at x_max is: {f_max:.5f}")
