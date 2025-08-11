def gauss_elimination(matrix):
    n = len(matrix)

    # Forward Elimination
    for i in range(n):
        # Making the diagonal element 1 (pivot)
        pivot = matrix[i][i]
        if pivot == 0:
            raise ValueError("Zero pivot encountered. Try rearranging the rows.")
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        # Eliminating the entries below the pivot
        for k in range(i + 1, n):
            factor = matrix[k][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]

    # Back Substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]

    return x

# Solving the following system:
# 2𝑥1 − 6𝑥2 − 𝑥3 = −38
# −3𝑥1 − 𝑥2 + 7𝑥3 = −34
# −8𝑥1 + 𝑥2 − 2𝑥3 = −20

aug_matrix = [
    [2, -6, -1, -38],
    [-3, -1, 7, -34],
    [-8, 1, -2, -20]
]

solution = gauss_elimination(aug_matrix)
print("Solution:", solution)
