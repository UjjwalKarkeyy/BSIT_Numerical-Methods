
import numpy as np

def my_func(x):
    return np.cos(x) + 3*x - 5
    # return x**2 + 1 # No root equation

def bisection_method(xl, xu, es, max_iter):
    if my_func(xl)*my_func(xu) > 0:
        print("Change initial guess value.")
        return False, None, None
    itr_count = 0
    xm_old = xl
    ea = 100
    print(f"{'Iter':<10}{'xl':<18}{'xu':<15}{'xm':<15}{'f(xl)':<15}{'f(xm)':<18}{'ea':<18}")
    while ea > es and itr_count < max_iter:
        xm = (xl + xu)/2
        if(itr_count > 0):
            ea = np.abs((xm - xm_old)/xm)*100
        xm_old= xm
        f_xm = my_func(xm)
        f_xl = my_func(xl)
        print(f'{(itr_count+1):<5}\t{xl:<10.6f}\t{xu:<10.6f}\t{xm:<10.6f}\t{f_xl:<10.6f}\t{f_xm:<10.6f}\t{ea:<10.6f}')
        if f_xm * f_xl < 0:
            xu = xm
        elif f_xm * f_xl > 0:
            xl = xm
        else:
            break
        itr_count += 1

    if(ea < es):
        return True, xm, ea
    else:
        return False, None, None
    
# Testing the function
xl = 1
xu = 2
es = 0.05
max_iter = 500
isRoot, root, absRelativeError = bisection_method(xl, xu, es, max_iter)
if(isRoot):
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f'Root is: {root:.4f}\nAbsolute Relative Error: {absRelativeError:.4f}%')

else:
    print("No root found.")