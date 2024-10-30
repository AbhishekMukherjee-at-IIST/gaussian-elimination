import numpy as np

def noPivot(matrix: np.ndarray):
    matrix = matrix.astype(np.float64)
    [m, _] = matrix.shape

    for i in range(0, m):
        for j in range(i+1, m):
            matrix[j] -= (matrix[j][i]/matrix[i][i]) * matrix[i]

    return matrix

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

def fullPivot(matrix: np.ndarray):
    matrix = matrix.astype(np.float64)
    [m, n] = matrix.shape

    permutationMatrix = np.identity(m)

    for i in range(0, m):
        maxValArg = abs(matrix[i : m, i : n-1]).argmax()
        maxR = int(maxValArg // (n-i-1)) + i
        maxC = int(maxValArg % (n-i-1)) + i

        # Column Swap
        if not(i == maxC):
            for row in range(0, m):
                matrix[row, i], matrix[row, maxC] = matrix[row, maxC], matrix[row, i]
                permutationMatrix[row, i], permutationMatrix[row, maxC] = permutationMatrix[row, maxC], permutationMatrix[row, i]

        # Row Swap
        if not(i == maxR):
            for col in range(0, n):
                matrix[i, col], matrix[maxR, col] = matrix[maxR, col], matrix[i, col]

        for j in range(i+1, m):
            matrix[j] -= (matrix[j][i]/matrix[i][i]) * matrix[i]

    return [matrix, permutationMatrix]

def backSubstitute(matrix: np.ndarray):
    # matrix is an augmented matrix
    [_, n] = matrix.shape
    n -= 1
    solution = np.zeros((n, 1))

    for i in range(n-1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += matrix[i, j] * solution[j]
        solution[i] = (matrix[i, -1] - sum)/(matrix[i, i])

    return solution