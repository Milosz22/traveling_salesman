import unittest
from App.app_functions import *


class MyTestCase(unittest.TestCase):
    def test_load_graph_from_file_1(self):
        # Given
        filepath = "Tests/test_load_1.txt"
        expected_result = [[3, 1], [20, 22], [5, 24], [7, 9]]

        # When
        result = load_graph_from_file_coordinates(filepath)

        # Then
        self.assertEqual(expected_result, result)

    def test_load_graph_from_file_2(self):
        # Given
        filepath = "Tests/test_load_.txt"
        expected_result = [[59, 49], [17, 93], [19, 43], [59, 86], [94, 66], [7, 6], [90, 87], [64, 86], [97, 84],
                           [9, 26], [23, 4], [80, 15], [5, 41], [33, 59], [60, 98]]

        # When
        result = load_graph_from_file_coordinates(filepath)

        # Then
        self.assertEqual(expected_result, result)

    def test_save_christo_graph_to_file_1(self):
        # Given
        filepath = "test_save_1.txt"
        graphToTest = {'0': {'1': 1, '2': 20, '3': 2}, '1': {'0': 1, '2': 28, '3': 5},
                       '2': {'0': 20, '1': 28, '3': 32}, '3': {'0': 2, '1': 5, '2': 32}}
        expected_result = "0\n2\n3\n1\n"

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
        expected_result = "0\n2\n3\n1\n"

        # When
        save_christo_graph_to_file(graphToTest, filepath)
        with open(filepath) as f:
            result = f.read()
        # print(str(result) == "0\n2\n3\n1\n")
        # print(len(result))

        # Then
        self.assertEqual(expected_result, result)

    def test_save_christo_graph_to_file_3(self):
        # Given
        filepath = "test_save_3.txt"
        graphToTest = {'0': {'1': 2, '2': 270, '3': 1000}, '1': {'0': 2, '2': 15, '3': 120},
                       '2': {'0': 270, '1': 15, '3': 50}, '3': {'0': 1000, '1': 120, '2': 50}}
        expected_result = "0\n3\n2\n1\n"

        # When
        save_christo_graph_to_file(graphToTest, filepath)
        with open(filepath) as f:
            result = f.read()

        # Then
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
