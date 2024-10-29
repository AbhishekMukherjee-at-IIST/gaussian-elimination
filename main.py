from noPivoting import noPivot
from partialPivoting import partialPivot
from fullPivoting import fullPivot
from backSubstitute import backSubstitute
import numpy as np

mat1 = np.array([[4, 0, -1, 10],
                [6, -8, -2, 6],
                [-1, 3, 0, 0]])

mat2 = np.array([[0, 2, 1, 5],
                 [1, -1, 1, 2],
                 [3, 1, -2, 1]])

mat3 = np.array([[0, -1, 1, 2],
                 [1, 2, 1, 5],
                 [3, 1, -2, 1]])

def printResults(matrix):
    print("\nNo Pivoting:")
    print(backSubstitute(noPivot(matrix)))

    print("\nPartial Pivoting:")
    print(backSubstitute(partialPivot(matrix)))

    print("\nFull Pivoting:")
    [A, P] = fullPivot(matrix)
    print(np.dot(P, backSubstitute(A)))

printResults(mat2)