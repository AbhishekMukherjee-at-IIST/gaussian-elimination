import numpy as np

def noPivot(matrix: np.ndarray):
    matrix = matrix.astype(np.float64)
    [m, _] = matrix.shape

    for i in range(0, m):
        



        for j in range(i+1, m):
            matrix[j] -= (matrix[j][i]/matrix[i][i]) * matrix[i]

    return matrix