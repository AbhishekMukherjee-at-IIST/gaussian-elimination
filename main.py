from noPivoting import noPivot
from partialPivoting import partialPivot
from backSubstitute import backSubstitute
import numpy as np

mat = np.array([[4, 0, -1, 10],
                [6, -8, -2, 6],
                [-1, 3, 0, 0]])

# print("No Pivoting:")
# print(noPivot(mat))
# print(backSubstitute(noPivot(mat)))

print("Partial Pivoting:")
print(partialPivot(mat))
print(backSubstitute(partialPivot(mat)))
