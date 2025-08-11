# def gauss_jordan(matrix):
#     n = len(matrix)

#     # Forward + Backward Elimination
#     for i in range(n):
#         # Making the pivot = 1
#         pivot = matrix[i][i]
#         if pivot == 0:
#             raise ValueError("Zero pivot encountered.")
#         for j in range(n + 1):
#             matrix[i][j] /= pivot

#         # Eliminating all other entries in column i
#         for k in range(n):
#             if k != i:
#                 factor = matrix[k][i]
#                 for j in range(n + 1):
#                     matrix[k][j] -= factor * matrix[i][j]

#     # Extracting solutions
#     return [row[-1] for row in matrix]

# # Solving the following system:
# # 2𝑥 + 3𝑦 − 𝑧 = 54
# # 𝑥 + 𝑦 + 𝑧 = 6
# # −2𝑥 + 5𝑦 + 2𝑧 = −3

# aug_matrix = [
#     [2,1,1,7],
#     [4,2,3,4],
#     [1,-1,1,0]
# ]

# solution = gauss_jordan(aug_matrix)
# print("Solution (Gauss-Jordan):", solution)



import numpy as np

def gauss_jordan(a, b):
    n = len(b)
    aug = np.hstack([a.astype(float), b.reshape(-1,1)])  # Augmented matrix

    for i in range(n):
        # Make the diagonal element 1
        aug[i] = aug[i] / aug[i][i]

        # Make all other elements in the column 0
        for j in range(n):
            if i != j:
                factor = aug[j][i]
                aug[j] = aug[j] - factor * aug[i]

    return aug[:, -1]  # Return the last column (solutions)

# Example system
A = np.array([
    [2,4,-6],
    [1,3,1],
    [2,-4,-2]
])

B = np.array([-8,10,-12])

solution = gauss_jordan(A, B)
print("Solution:", solution)
