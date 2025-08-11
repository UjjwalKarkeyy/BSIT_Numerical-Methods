from scipy.misc import derivative as derv
import math
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def my_func(x):
    return math.exp(-0.5*x)*(4 - x) - 2
    # return x**2 + 1 # No equation root

def func_derivation(x):
    return derv(my_func, x)

def newton_raphson_method(xi, es, max_itr):
    itr_count = 0
    ea = 100
    print(f"{'Iter':<10}{'xi':<15}{'xi_new':<18}{'f(xi)':<15}{'f_p(xi)':<18}{'ea':<18}")
    while ea > es and itr_count < max_itr:
        f_xi = my_func(xi)
        f_xi_prime = func_derivation(xi)
        if f_xi_prime == 0:
            print("Division by zero. Stopping iteration!")
            break
        xi_new = xi - (f_xi/f_xi_prime)
        ea = abs((xi_new - xi)/xi_new)*100
        xi = xi_new
        print(f'{(itr_count+1):<5}\t{xi:<10.6f}\t{xi_new:<10.6f}\t{f_xi:<10.6f}\t{f_xi_prime:<10.6f}\t{ea:<10.6f}')
        itr_count += 1
    
    if(ea < es):
        return True, xi, ea
    else:
        return False, None, None
xi = 1
es = 5
max_itr = 500
isRoot, root, error = newton_raphson_method(xi, es, max_itr)
if(isRoot):
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"Root: {root:.4f}\nErro: {error:.4f}%")
else:
    print("There's no root for this equation!")
