import unittest
from App.app_functions import *
from Christofides.christofides import *


class MyTestCase(unittest.TestCase):
    def test_load_graph_from_file_1(self):
        # Given
        filepath = "test_load_1.txt"
        expected_result = {"0": {"1": 1, "2": 2}, "1": {"0": 1, "2": 2}, "2": {"0": 2, "1": 2}}

        # When
        result = load_graph_from_file(filepath)

        # Then
        self.assertEqual(expected_result, result)

    def test_load_graph_from_file_2(self):
        # Given
        filepath = "test_load_2.txt"
        expected_result = {"0": {"1": 1, "2": 2, "3": 3}, "1": {"0": 1, "2": 2, "3": 3}, "2": {"0": 2, "1": 2, "3": 3},
                           "3": {"0": 3, "1": 3, "2": 3}}

        # When
        result = load_graph_from_file(filepath)

        # Then
        self.assertEqual(expected_result, result)

    def test_load_graph_from_file_3(self):
        # Given
        filepath = "test_load_3.txt"
        expected_result = {"0": {"1": 1}, "1": {"0": 1}}

        # When
        result = load_graph_from_file(filepath)

        # Then
        self.assertEqual(expected_result, result)

    def test_save_christo_graph_to_file_1(self):
        # Given
        filepath = "test_save_1.txt"
        graphToTest = {'0': {'1': 1, '2': 20, '3': 2}, '1': {'0': 1, '2': 28, '3': 5},
                       '2': {'0': 20, '1': 28, '3': 32}, '3': {'0': 2, '1': 5, '2': 32}}
        expected_result = str(christofides(graph(graphToTest)))
        expected_result = "".join(
            c for c in expected_result if c.isdigit())

        # When
        save_christo_graph_to_file(graphToTest, filepath)
        with open(filepath) as f:
            result = f.read()

        # Then
        self.assertEqual(expected_result, result)

    def test_save_christo_graph_to_file_2(self):
        # Given
        filepath = "test_save_2.txt"
        graphToTest = {'0': {'1': 1, '2': 20, '3': 2}, '1': {'0': 1, '2': 28, '3': 5},
                       '2': {'0': 20, '1': 28, '3': 32}, '3': {'0': 2, '1': 5, '2': 32}}
        expected_result = str(christofides(graph(graphToTest)))
        expected_result = "".join(
            c for c in expected_result if c.isdigit())

        # When
        save_christo_graph_to_file(graphToTest, filepath)
        with open(filepath) as f:
            result = f.read()

        # Then
        self.assertEqual(expected_result, result)

    def test_save_christo_graph_to_file_3(self):
        # Given
        filepath = "test_save_3.txt"
        graphToTest = {'0': {'1': 2, '2': 270, '3': 1000}, '1': {'0': 2, '2': 15, '3': 120},
                       '2': {'0': 270, '1': 15, '3': 50}, '3': {'0': 1000, '1': 120, '2': 50}}
        expected_result = str(christofides(graph(graphToTest)))
        expected_result = "".join(
            c for c in expected_result if c.isdigit())

        # When
        save_christo_graph_to_file(graphToTest, filepath)
        with open(filepath) as f:
            result = f.read()

        # Then
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
