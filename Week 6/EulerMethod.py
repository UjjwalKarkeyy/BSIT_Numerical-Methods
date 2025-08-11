def func(x,y):
    return (y * (x ** 3)) - (1.5 * y)
    
def EulerMethod(x_given, y_given, x_pred, h, x):
    x_prev = x_given
    y_prev = y_given
    while(x <= x_pred):
        y = y_prev + (h*func(x_prev, y_prev))
        x_prev = x
        y_prev = y
        print(f'y({x}): {y}')
        x += h
        
x_given = 0
y_given = 1
x_pred = 2
# h = 0.5
h = 0.25
x = x_given + h
print(f'y({x_given}): {y_given}')
EulerMethod(x_given, y_given, x_pred, h, x)
