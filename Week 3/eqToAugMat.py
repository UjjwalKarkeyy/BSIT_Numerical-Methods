from sympy import symbols
import numpy as np

def extract_coeff(eq):
    x,y,z = symbols('x y z')
    expr = eq.lhs - eq.rhs # E.x: lhs = 2x+3y, rhs = 5, then lhs - rhs = 2x+3y-5 (This is an expression, no longer a equation) 
    coeffs = expr.as_coefficients_dict()
    coeff_x = coeffs.get(x,0)
    coeff_y = coeffs.get(y,0)
    coeff_z = coeffs.get(z,0)

    '''
        Here, get takes two arguments: First is the variable we are checking for like x,y, and z. If it gets the coefficient value, it returns the value else it returns 0. Similarly, for constant values, we've '1' as its coefficient so its like -5 * 1. It checks for 1 and returns the value if it gets it else returns zero. Also, we use a subtract sign here as while moving from rhs to lhs, it's sign changes i.e., 2x + 3y - 5 is actually, 2x + 3y = 5.
    '''
    constant = - coeffs.get(1,0)
    data = [coeff_x, coeff_y, coeff_z, constant]
    return data

def create_matrix(data1, data2, data3):
    new_data = [data1, data2, data3]
    aug_matrix = np.matrix(new_data)

    return aug_matrix

def eqToAugMain(*args):
    eq1 = args[0]
    eq2 = args[1]
    eq3 = args[2]
    data1 = extract_coeff(eq1)
    data2 = extract_coeff(eq2)
    data3 = extract_coeff(eq3)
    aug_matrix = create_matrix(data1, data2, data3)
    return aug_matrix