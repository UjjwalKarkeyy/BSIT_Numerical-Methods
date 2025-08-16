import numpy as np
import matplotlib.pyplot as plt

# Define the function to minimize (e.g., f(x) = x^2)
def f(x):
    return x**2

# Define the derivative of the function (e.g., f'(x) = 2x)
def gradient(x):
    return 2 * x

# Gradient Descent parameters
learning_rate = 0.1  # Step size for each iteration
iterations = 50      # Number of iterations
initial_x = 10.0     # Starting point

# Store the history of x values for visualization
x_history = [initial_x]

# Perform Gradient Descent
x = initial_x
for i in range(iterations):
    grad = gradient(x)
    x = x - learning_rate * grad
    x_history.append(x)

# Plot the function and the gradient descent path
x_vals = np.linspace(-12, 12, 400)
y_vals = f(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='f(x) = x^2')
plt.scatter(x_history, [f(val) for val in x_history], color='red', marker='o', label='Gradient Descent Path')
plt.title('Gradient Descent to Minimize f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()

print(f"Minimum found at x = {x_history[-1]:.4f}")
print(f"Minimum value of f(x) = {f(x_history[-1]):.4f}")