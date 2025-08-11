import sympy as sp

# define symbols
t, y = sp.symbols('t y')
C = sp.symbols('C')

# Left-hand and right-hand parts of separated equation
lhs = 1/y
rhs = t**3 - 1.5

# integrate both sides
int_lhs = sp.integrate(lhs, y)   # ln(y)
int_rhs = sp.integrate(rhs, t)   # t^4/4 - 1.5*t

# general solution form: ln(y) = t^4/4 - 1.5*t + C
general_eq = sp.Eq(int_lhs, int_rhs + C)

# solve for y
y_expr = sp.exp(int_rhs + C)

# apply initial condition y(0) = 1 to solve for C
C_val = sp.solve(sp.Eq(y_expr.subs(t, 0), 1), C)[0]

# final explicit solution
y_final = y_expr.subs(C, C_val)

# value at t = 2
y_at_2 = y_final.subs(t, 2).evalf()

print("C =", C_val)
print("y(t) =", y_final)
print("y(2) =", y_at_2)
