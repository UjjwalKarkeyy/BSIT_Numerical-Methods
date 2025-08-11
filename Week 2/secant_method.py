import math
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def my_func(x):
    return math.exp(x) + 3*x - 5
    # return x**2 + 1 # No equation root

def secant_method(xi, xi_prev, es, max_itr):
    itr_count = 0
    ea = 100
    print(f"{'Iter':<10}{'xi':<15}{'xi_prev':<15}{'xi_new':<18}{'f(xi)':<15}{'f(xi_prev))':<18}{'ea':<18}")
    while ea > es and itr_count < max_itr:
        f_xi = my_func(xi)
        f_xi_prev = my_func(xi_prev)
        xi_new = xi - (f_xi * (xi - xi_prev)/(f_xi - f_xi_prev))
        ea = abs((xi_new - xi)/xi_new)*100
        xi_prev = xi
        xi = xi_new
        print(f'{(itr_count+1):<5}\t{xi:<10.6f}\t{xi_prev:<10.6f}\t{xi_new:<10.6f}\t{f_xi:<10.6f}\t{f_xi_prev:<10.6f}\t{ea:<10.6f}')
        itr_count += 1

    if(ea < es):
        return True, xi, ea
    else:
        return False, None, None

xi = 1
xi_prev = 0.5
es = 5
max_itr = 500
isRoot, root, error = secant_method(xi, xi_prev, es, max_itr)
if(isRoot):
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"Root: {root:.4f}\nErro: {error:.4f}%")
else:
    print("No root for this equation!")
