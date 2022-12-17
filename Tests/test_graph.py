import unittest
from Christofides.graph import *


class MyTestCase(unittest.TestCase):

    def test_init_nx(self):
        # Given
        G1 = nx.path_graph(4)
        for i in range(3):
            G1[i + 1][i]["weight"] = i * i + 1
        G1_graph = graph(G1)
        expected_result = {"0": {"1": 1}, "1": {"0": 1, "2": 2}, "2": {"1": 2, "3": 5}, "3": {"2": 5}}

        # When
        result = G1_graph.G

        # Then
        self.assertEqual(expected_result, result)

    def test_init_matrix(self):
        # Given
        G1 = [[0, 1, 0, 0],
              [1, 0, 2, 0],
              [0, 2, 0, 5],
              [0, 0, 5, 0]]
        G1_graph = graph(G1)
        expected_result = {0: {1: 1}, 1: {0: 1, 2: 2}, 2: {1: 2, 3: 5}, 3: {2: 5}}

        # When
        result = G1_graph.G

        # Then
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
