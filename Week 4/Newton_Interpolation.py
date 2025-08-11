import numpy as np

def divided_diff(x, y):
    n = len(y)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j - 1]) / (x[j:n] - x[j - 1])
    return coef

def newton_poly(coef, x_data, x):
    n = len(coef) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

def print_divided_diff_table(x, y):
    n = len(x)
    table = np.zeros((n, n))
    table[:,0] = y
    # Filling the divided difference table
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])
    headers = [f"f[x{i}" + (f",...,x{i+j}]" if j > 0 else "]") for j in range(n) for i in range(n-j)]
    print("\nDivided Difference Table:")
    print("-" * (15 * n))
    for i in range(n):
        row = ""
        for j in range(n):
            if j <= n - i - 1:
                row += f"{table[i][j]:<15.6f}"
            else:
                row += " " * 15
        print(row)
    print("-" * (15 * n))
# Data
x_data = np.array([1,2,3,4,5])
y_data = np.array([0,7,26,63,124])
print_divided_diff_table(x_data, y_data)
# Calculate interpolation
a = divided_diff(x_data, y_data)
x_pred = 1.5
predicted_value = newton_poly(a, x_data, x_pred)
print(f"\nEstimated value for {x_pred} is: {predicted_value:.2f}")
