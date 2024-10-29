import numpy as np

def backSubstitute(matrix: np.ndarray):
    # matrix is an augmented matrix
    [_, n] = matrix.shape
    n -= 1
    solution = np.zeros((n, 1))

    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += matrix[i, j] * solution[j]
        solution[i] = (matrix[i][-1]-sum)/(matrix[i][i])

    return solution

# okay, tested!
