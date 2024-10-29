import numpy as np

def conditionNumber(matrix):
    pass

def gaussElimination(matrix):
    """Returns the solution matrix of a system of linear equations

    Args:
        matrix (NDArray[any]): Augmented matrix of size (n) x (n + 1)

    Returns:
        NDArray[float64]: Row vector of size n consisting solutions of the system of linear equations
    """    
    matrix = matrix.astype(np.float64)              # To ensure values are always of float datatype
    
    (rows, cols) = np.shape(matrix)
    solution = np.zeros(cols - 1)
    
    for pivotRow in range(0, rows - 1):                                      
        # Partial Pivot Algorithm
        if matrix[pivotRow][pivotRow] == 0:
            maxValRow = pivotRow + np.argmax(matrix[pivotRow + 1:rows, pivotRow]) + 1
            # Algorithm to exchange/swap two rows
            for c in range(0, cols):
                matrix[pivotRow][c], matrix[maxValRow][c] = matrix[maxValRow][c], matrix[pivotRow][c]    
        
        # Alternative algorithm to replace a zero pivot row with the next non-zero pivot row
        # r = ucRow + 1
        # while matrix[ucRow][ucRow] == 0:
        #     for c in range(0, cols):
        #         matrix[ucRow][c], matrix[r][c] = matrix[r][c], matrix[ucRow][c]
        #     r += 1  
                            
        # Gaussian Elimination Algorithm        
        for row in range(pivotRow + 1, rows):
            alpha = matrix[row][pivotRow]/matrix[pivotRow][pivotRow]
            matrix[row] -= alpha * matrix[pivotRow]
       
    diagonalProduct = 1   
    for i in range(0, rows):
        diagonalProduct *= matrix[i][i]
            
    if diagonalProduct == 0:
        if matrix[-1][-1] == 0:
            return ["Infinite Solutions"]
        else:
            return ["No Solutions"]
    
    # Back Substitution Algorithm            
    for sRow in range(cols - 2, -1, -1):                            # sRow = Solution Row
        beta = 0                                                
        for k in range(sRow + 1, rows):                                                        
            beta += matrix[sRow][k] * solution[k]
            
        solution[sRow] = (matrix[sRow][cols - 1] - beta) / matrix[sRow][sRow]
    return solution

test1 = {
    "matrix": np.array([[6, -8, -2, 6],[4, 0, -1, 10],[-1, 3, 0, 0]]),
    "solution": [3, 1, 2] 
}

test2 = {
    "matrix": np.array([[3, 4, 11], [9, 2, 8]]),
    "solution": [1/3, 5/2]
}

test3 = {
    "matrix": np.array([[1, 1, 1, 4], [2, 2, 3, 9], [3, 4, -2, 9]]),
    "solution": [1, 2, 1]
}

test4 = {
    "matrix": np.array([[1, 2, 5],[2, 4, 8]]),
    "solution": ["No Solutions"]
}

test5 = {
    "matrix": np.array([[1, 2, 5, 9], [2, 3, 8, 2], [5, 10, 25, 45]]),
    "solution": ["Infinite Solutions"]
}

tests = [test1, test2, test3, test4, test5]

for i in range(0,len(tests)):
    print(f"\n\nTest #{i+1} - ")
    print(f"Matrix: \n{tests[i].get('matrix')}")
    solution = gaussElimination(tests[i].get('matrix'))
    
    print(f"\nExpected Solution: {tests[i].get('solution')}")
    print(f"Actual Solution: {solution}")
    if (tests[i].get("solution") and solution).all() :
        print("Test Passed")
    else:
        print("Test Failed")
