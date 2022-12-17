import unittest
from Christofides.kruskal import *
from Christofides.graph import *


class MyTestCase(unittest.TestCase):

    # I'm testing the "is_path" function

    def test_is_path_1(self):
        # Given
        F = graph([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]]).G
        a = 0
        b = 1
        expected_result = True

        # When
        result = is_path(F, a, b)

        # Then
        self.assertEqual(expected_result, result)

    def test_is_path_2(self):
        # Given
        H = graph([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]).G
        a = 0
        b = 3
        expected_result = False

        # When
        result = is_path(H, a, b)

        # Then
        self.assertEqual(expected_result, result)

    def test_is_path_3(self):
        # Given
        E = graph([[0, 1], [1, 0]]).G
        a = 0
        b = 0
        expected_result = True

        # When
        result = is_path(E, a, b)

        # Then
        self.assertEqual(expected_result, result)

    def test_is_path_4(self):
        # Given
        F = graph([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]]).G
        a = 1
        b = 2
        expected_result = True

        # When
        result = is_path(F, a, b)

        # Then
        self.assertEqual(expected_result, result)

    def test_is_path_5(self):
        # Given
        K = graph([[0, 0, 0], [0, 0, 0], [0, 0, 0]]).G
        a = 0
        b = 10
        expected_result = False

        # When
        result = is_path(K, a, b)

        # Then
        self.assertEqual(expected_result, result)

    # I'm testing the "add_edge_cycle" function

    def test_add_edge_cycle_1(self):
        # Given
        F = graph([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]]).G
        a = 0
        b = 1
        expected_result = False

        # When
        result = add_edge_cycle(F, a, b)

        # Then
        self.assertEqual(expected_result, result)

    def test_add_edge_cycle_2(self):
        # Given
        H = graph([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]).G
        a = 0
        b = 1
        expected_result = False

        # When
        result = add_edge_cycle(H, a, b)

        # Then
        self.assertEqual(expected_result, result)

    def test_add_edge_cycle_3(self):
        # Given
        F = graph([[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0]]).G
        a = 2
        b = 3
        expected_result = True

        # When
        result = add_edge_cycle(F, a, b)

        # Then
        self.assertEqual(expected_result, result)

    def test_add_edge_cycle_4(self):
        # Given
        H = graph([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]]).G
        a = 0
        b = 1
        expected_result = False

        # When
        result = add_edge_cycle(H, a, b)

        # Then
        self.assertEqual(expected_result, result)

    def test_add_edge_cycle_5(self):
        # Given
        K = graph([[0, 0, 0], [0, 0, 0], [0, 0, 0]]).G
        a = 1
        b = 2
        expected_result = False

        # When
        result = add_edge_cycle(K, a, b)

        # Then
        self.assertEqual(expected_result, result)

    # I'm testing the "find_min_weight" function

    def test_find_min_weight_1(self):
        # Given
        G1 = graph({'0': {'1': 0.1, '2': 0.2}, '1': {'0': 0.1}, '2': {'0': 0.2}}).G
        expected_result = ['0', '1', 0.1]

        # When
        result = find_min_weight(G1)

        # Then
        self.assertEqual(expected_result, result)

    def test_find_min_weight_2(self):
        # Given
        G2 = graph({'0': {'1': 3.2}, '1': {'1': 3.2}, '2': {}}).G
        expected_result = ['0', '1', 3.2]

        # When
        result = find_min_weight(G2)

        # Then
        self.assertEqual(expected_result, result)

    def test_find_min_weight_3(self):
        # Given
        G2 = graph({'0': {}, '1': {}, '2': {}}).G
        expected_result = False
        # When
        result = find_min_weight(G2)

        # Then
        self.assertEqual(expected_result, result)

    # I'm testing the "kruskal" function
    def test_kruskal_1(self):
        # Given
        G3 = graph({'0': {'1': 0.1, '2': 0.2, '3': 0.3}, '1': {'0': 0.1, '2': 0.3, '3': 0.4},
                    '2': {'0': 0.2, '1': 0.3, '3': 0.5}, '3': {'0': 0.3, '1': 0.4, '2': 0.5}})
        expected_result = graph({'0': {'1': 0.1, '2': 0.2, '3': 0.3}, '1': {'0': 0.1}, '2': {'0': 0.2},
                                 '3': {'0': 0.3}}).G

        # When
        result = kruskal(G3)

        # Then
        self.assertEqual(result, expected_result)

    def test_kruskal_2(self):
        # Given
        G4 = graph({'0': {'1': 1, '2': 2, '4': 4}, '1': {'0': 1, '2': 2, '3': 5},
                    '2': {'0': 2, '1': 2, '3': 2, '4': 2}, '3': {'1': 5, '2': 2, '4': 1},
                    '4': {'0': 4, '2': 2, '3': 1}})
        expected_result = graph({'0': {'1': 1, '2': 2}, '1': {'0': 1}, '2': {'0': 2, '3': 2},
                                 '3': {'2': 2, '4': 1}, '4': {'3': 1}, }).G

        # When
        result = kruskal(G4)

        # Then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
