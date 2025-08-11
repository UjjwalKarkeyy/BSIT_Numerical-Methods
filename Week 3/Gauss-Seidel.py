def is_diagonally_dominant(a):
    n = len(a)
    for i in range(n):
        diag = abs(a[i][i])
        off_diag_sum = sum(abs(a[i][j]) for j in range(n) if j != i)
        if diag <= off_diag_sum:
            return False
    return True

def gauss_seidel(a, b, x0=None, iterations=25, tolerance=1e-10):
    n = len(a)

    if not is_diagonally_dominant(a):
        print("Warning: Matrix is not diagonally dominant. Gauss-Seidel may not converge.")

    x = x0[:] if x0 else [0] * n

    for _ in range(iterations):
        x_new = x[:]
        for i in range(n):
            sum_ = sum(a[i][j] * x_new[j] if j < i else a[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_) / a[i][i]

        # Checking for convergence
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new

        x = x_new

    return x  # Returning result after max iterations even if not converged

# Solving the following system:
# −3𝑥 + 𝑦 + 15𝑧 = 44
# 6𝑥 − 2𝑦 + 𝑧 = 5
# 5𝑥 + 10𝑦 + 𝑧 = 28

A = [
    [12,4,-6],
    [1,3,6],
    [2,-4,-1],
]
B = [-8,10,-12]

solution = gauss_seidel(A, B)
print("Solution (Gauss-Seidel):", solution)
