import numpy as np

def partialPivot(matrix: np.ndarray):
    matrix = matrix.astype(np.float64)
    [m, n] = matrix.shape

    for i in range(0, m):
        maxValRow = matrix[i : m, i].argmax() + i
        if not(i == maxValRow):
            for col in range(0, n):
                matrix[i, col], matrix[maxValRow, col] = matrix[maxValRow, col], matrix[i, col]

        for j in range(i+1, m):
            matrix[j] -= (matrix[j][i]/matrix[i][i]) * matrix[i]

    return matrix