x = [1,2,3,4]
y = [0,0.3010,0.4771,0.6021] # In Fahrenheit

n = len(x)
x_pred = 2.5

def main_func():
    ans = 0
    for i in range(n):
        l_val = side_func(i)
        ans = ans + (y[i] * l_val)

    print(f"Predicted value for {x_pred} is: {ans}") 

def side_func(i):
    numerator = denomenator = 1
    for j in range(n):
        if(j != i):
            numerator *= (x_pred - x[j])
            denomenator *= (x[i] - x[j])
    return float(numerator/denomenator)

main_func()