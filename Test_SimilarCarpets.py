import unittest
import numpy as np
from Project import find_similar_carpet

class TestProject(unittest.TestCase):
    def test_find_similar_carpet(self):
        input_map = np.array([[1, 2, 3], [4, 5, 6]])
        carpet_maps = [
            np.array([[1, 2, 3], [4, 5, 6]]),
            np.array([[7, 8, 9], [10, 11, 12]]),
            np.array([[1, 2, 3], [4, 0, 6]]),
        ]
        num_similar = 2
        expected_result = [0, 2]

        result = find_similar_carpet(input_map, carpet_maps, num_similar)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
