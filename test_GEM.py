import unittest
import gaussianElimination as GEM
import numpy as np

class TestGEM(unittest.TestCase):
    
    def setUp(self):
        self.mat1 = np.array([[4, 0, -1, 10],
                [6, -8, -2, 6],
                [-1, 3, 0, 0]])
        self.mat1_sol = [3, 1, 2]

        self.mat2 = np.array([[0, 2, 1, 5],
                    [1, -1, 1, 2],
                    [3, 1, -2, 1]])
        self.mat2_sol = [[1.28571429], [1.42857143]
 [2.14285714]]

        self.mat3 = np.array([[0, -1, 1, 2],
                    [1, 2, 1, 5],
                    [3, 1, -2, 1]])
        self.mat3_sol = []

    def test_noPivot(self):
        self.assertEqual(GEM.noPivot(self.mat1), self.mat1_sol)
        self.assertEqual(GEM.noPivot(self.mat2), self.mat2_sol)
        self.assertEqual(GEM.noPivot(self.mat3), self.mat3_sol)


if __name__ == "__main__":
    unittest.main()