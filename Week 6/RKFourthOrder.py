def func(x,y):
    # return (y * (x ** 3)) - (1.5 * y)
    return (1 + 2*y) * (x ** 0.5)

def RKFourthOrder(x_given, y_given, x_pred, h, x):
    x_prev = x_given
    y_prev = y_given
    while(x <= x_pred):
        k1 = func(x_prev, y_prev)
        k2 = func((x_prev + (0.5 * h)), (y_prev + (0.5 * k1 * h)))
        k3 = func((x_prev + (0.5 * h)), (y_prev + (0.5 * k2 * h)))
        k4 = func((x_prev + h), (y_prev + (k3 * h)))
        y = y_prev + ((1 / 6) * (k1 + (2*k2) + (2*k3) + k4) * h)
        x_prev = x
        y_prev = y
        print(f'y({x}): {y}')
        x += h        
    return y

x_given = 0
y_given = 1
x_pred = 1
h = 0.5
x = x_given + h
print(f'y({x_given}): {y_given}')
RKFourthOrder(x_given, y_given, x_pred, h, x)  