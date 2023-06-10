import unittest
from Project import find_shortest_path

class TestProject(unittest.TestCase):
    def test_find_shortest_path(self):
        map_graph = {
            'Intersection1': {'Intersection2': 10, 'Intersection3': 5},
            'Intersection2': {'Intersection1': 10, 'Intersection4': 1},
            'Intersection3': {'Intersection1': 5, 'Intersection4': 5},
            'Intersection4': {'Intersection2': 1, 'Intersection3': 5, 'Intersection5': 3},
            'Intersection5': {'Intersection4': 3}
        }

        branches = {
            'Branch1': 'Intersection2',
            'Branch2': 'Intersection4',
            'Branch3': 'Intersection5'
        }
        user_location = 'Intersection5'
        destination_branch = 'Branch2'
        expected_result = ["Intersection5" , "Intersection4"]

        path_to_branch = find_shortest_path(map_graph, user_location, branches[destination_branch])
        self.assertEqual(path_to_branch, expected_result)

if __name__ == '__main__':
    unittest.main()
