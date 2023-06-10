import unittest
import sys
sys.path.insert(0, '..')
from Project import find_similar_carpet

# Rest of your test code

from Project import find_affordable_carpets

class TestProject(unittest.TestCase):
    def test_find_affordable_carpets(self):
        carpet_prices = [10, 20, 30, 40, 50]
        max_budget = 100
        expected_result = [40, 30, 20, 10]

        result = find_affordable_carpets(carpet_prices, max_budget)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
