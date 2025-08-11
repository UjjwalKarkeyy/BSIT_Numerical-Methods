import numpy as np

x_data = np.array([2,7,11,12])
y_data = np.array([5,8,15,20])
n = 4
x_pred = 11.5

def finding_range():
    for i in range(n):
        if(x_data[i] <= x_pred >= x_data[i+1]):
            return x_data[i], x_data[i+1]
        
def upper_range():
    for x in x_data:
        if(x >= x_pred):
            return x
        
def select_range():
    
       
    lower_x_indx = [i for i,val in enumerate(x_data) if val == lower_range_x]
    upper_x_indx = [i for i,val in enumerate(x_data) if val == upper_range_x]

    return lower_range_x, upper_range_x, lower_x_indx, upper_x_indx

def linear_interpolation(x_values, y_values, x):
    results = y_values[0] + (x - x_values[0])*(y_values[1] - y_values[0]) / (x_values[1] - x_values[0])
    return results

x1, x2, y1_indx, y2_indx = select_range()
x_values = np.array([x1,x2])
y_values = np.array([y_data[y1_indx], y_data[y2_indx]])
print(x_values)
print(y_values)

# answer = linear_interpolation(x_values, y_values, x)
# print(answer)