import unittest
from Christofides.christofides import *
from Christofides.graph import *


class MyTestCase(unittest.TestCase):

    # I'm testing the "odd_deg_vertices" function

    def test_odd_deg_vertices1(self):
        # Given
        G1 = graph({'0': {'1': 10, '2': 8}, '1': {'0': 10, '2': 2, '3': 5, '4': 6},
                    '2': {'0': 8, '1': 2}, '3': {'1': 5, '4': 1},
                    '4': {'1': 6, '3': 1}})
        expected_result = []

        # When
        result = odd_deg_vertices(G1)

        # Then
        self.assertEqual(expected_result, result)

    def test_odd_deg_vertices2(self):
        # Given
        G2 = graph({'0': {'2': 2, '3': 2}, '1': {'2': 2, '3': 5},
                    '2': {'0': 2, '1': 2, '3': 2}, '3': {'0': 2, '1': 5, '2': 2}})
        expected_result = ['2', '3']

        # When
        result = odd_deg_vertices(G2)

        # Then
        self.assertEqual(expected_result, result)

    def test_odd_deg_vertices3(self):
        # Given
        G3 = graph({'0': {'1': 0.1, '2': 2.5, '3': 2.8}, '1': {'0': 8, '2': 2, '3': 15},
                    '2': {'0': 27.5, '1': 102, '3': 4.2}, '3': {'0': 32, '1': 5, '2': 0.2}})
        expected_result = ['0', '1', '2', '3']

        # When
        result = odd_deg_vertices(G3)

        # Then
        self.assertEqual(expected_result, result)

    # I'm testing the "ham_from_eul" function

    def test_ham_from_eul1(self):
        # Given
        E1 = nx.eulerian_circuit(graph({'0': {'1': 1, '4': 4}, '1': {'0': 1, '2': 2, '3': 5, '4': 6},
                                        '2': {'1': 2, '3': 2}, '3': {'1': 5, '2': 2},
                                        '4': {'0': 4, '1': 6}}).to_nx())

        expected_result1 = ['1', '0', '4', '3', '2']
        expected_result2 = ['2', '1', '0', '4', '3']
        expected_result3 = ['3', '2', '1', '0', '4']
        expected_result4 = ['4', '3', '2', '1', '0']
        expected_result5 = ['0', '4', '3', '2', '1']
        expected_result6 = ['1', '2', '3', '4', '0']
        expected_result7 = ['0', '1', '2', '3', '4']
        expected_result8 = ['4', '0', '1', '2', '3']
        expected_result9 = ['3', '4', '0', '1', '2']
        expected_result10 = ['2', '3', '4', '0', '1']
        expected_result11 = ['1', '0', '4', '2', '3']
        expected_result12 = ['3', '1', '0', '4', '2']
        expected_result13 = ['2', '3', '1', '0', '4']
        expected_result14 = ['4', '2', '3', '1', '0']
        expected_result15 = ['0', '4', '2', '3', '1']
        expected_result16 = ['1', '2', '3', '0', '4']
        expected_result17 = ['4', '1', '2', '3', '0']
        expected_result18 = ['0', '4', '1', '2', '3']
        expected_result19 = ['3', '0', '4', '1', '2']
        expected_result20 = ['2', '3', '0', '4', '1']
        expected_result21 = ['1', '3', '2', '0', '4']
        expected_result22 = ['4', '1', '3', '2', '0']
        expected_result23 = ['0', '4', '1', '3', '2']
        expected_result24 = ['2', '0', '4', '1', '3']
        expected_result25 = ['3', '2', '0', '4', '1']
        expected_result26 = ['1', '3', '2', '4', '0']
        expected_result27 = ['0', '1', '3', '2', '4']
        expected_result28 = ['4', '0', '1', '3', '2']
        expected_result29 = ['2', '4', '0', '1', '3']
        expected_result30 = ['3', '2', '4', '0', '1']

        # When
        result = ham_from_eul(E1)

        # Then
        self.assertTrue(result in [expected_result1, expected_result2, expected_result3, expected_result4,
                                   expected_result5, expected_result6, expected_result7, expected_result8,
                                   expected_result9, expected_result10, expected_result11, expected_result12,
                                   expected_result13, expected_result14, expected_result15, expected_result16,
                                   expected_result17, expected_result18, expected_result19, expected_result20,
                                   expected_result21, expected_result22, expected_result23, expected_result24,
                                   expected_result25, expected_result26, expected_result27, expected_result28,
                                   expected_result29, expected_result30])

    def test_ham_from_eul2(self):
        # Given
        E2 = nx.eulerian_circuit(graph({'0': {'2': 2, '3': 2}, '1': {'2': 2, '3': 5},
                                        '2': {'0': 2, '1': 2}, '3': {'0': 2, '1': 5}}).to_nx())
        expected_result1 = ['0', '2', '1', '3']
        expected_result2 = ['3', '0', '2', '1']
        expected_result3 = ['1', '3', '0', '2']
        expected_result4 = ['2', '1', '3', '0']
        expected_result5 = ['0', '3', '1', '2']
        expected_result6 = ['2', '0', '3', '1']
        expected_result7 = ['1', '2', '0', '3']
        expected_result8 = ['3', '1', '2', '0']

        # When
        result = ham_from_eul(E2)

        # Then
        self.assertTrue(result in [expected_result1, expected_result2, expected_result3, expected_result4,
                                   expected_result5, expected_result6, expected_result7, expected_result8])

    def test_ham_from_eul3(self):
        # Given
        E3 = nx.eulerian_circuit(graph({'0': {'1': 1, '2': 2}, '1': {'0': 1, '2': 2}, '2': {'0': 2, '1': 2}}).to_nx())

        expected_result1 = ['0', '1', '2']
        expected_result2 = ['0', '2', '1']
        expected_result3 = ['1', '2', '0']
        expected_result4 = ['2', '1', '0']
        expected_result5 = ['2', '0', '1']
        expected_result6 = ['1', '0', '2']

        # When
        result = ham_from_eul(E3)

        # Then
        self.assertTrue(result in [expected_result1, expected_result2, expected_result3,
                                   expected_result4, expected_result5, expected_result6])

    # I'm testing the "christofides" function

    def test_christofides1(self):
        # Given
        D1 = graph({'0': {'1': 1, '2': 30, '3': 2}, '1': {'0': 1, '2': 29, '3': 3},
                    '2': {'0': 30, '1': 29, '3': 32}, '3': {'0': 2, '1': 3, '2': 32}})
        expected_result1 = ['0', '3', '2', '1']
        expected_result2 = ['1', '0', '3', '2']
        expected_result3 = ['2', '1', '0', '3']
        expected_result4 = ['3', '2', '1', '0']
        expected_result5 = ['0', '1', '2', '3']
        expected_result6 = ['3', '0', '1', '2']
        expected_result7 = ['2', '3', '0', '1']
        expected_result8 = ['1', '2', '3', '0']

        # When
        result = christofides(D1)

        result_cost = 0
        for k in range(len(result) - 1):
            result_cost = result_cost + D1.G[result[k]][result[k + 1]]

        result_cost = result_cost + D1.G[result[0]][result[len(result) - 1]]

        # Then
        self.assertTrue(result in [expected_result1, expected_result2, expected_result3, expected_result4,
                                   expected_result5, expected_result6, expected_result7, expected_result8
                                   and result_cost <= 96])

    def test_christofides2(self):
        # Given
        D2 = graph({'0': {'1': 3, '2': 3}, '1': {'0': 3, '2': 3}, '2': {'0': 3, '1': 3}})
        expected_result1 = ['0', '1', '2']
        expected_result2 = ['0', '2', '1']
        expected_result3 = ['1', '2', '0']
        expected_result4 = ['2', '1', '0']
        expected_result5 = ['2', '0', '1']
        expected_result6 = ['1', '0', '2']

        # When
        result = christofides(D2)

        result_cost = 0
        for k in range(len(result) - 1):
            result_cost = result_cost + D2.G[result[k]][result[k + 1]]

        result_cost = result_cost + D2.G[result[0]][result[len(result) - 1]]

        # Then
        self.assertTrue(result in [expected_result1, expected_result2, expected_result3,
                                   expected_result4, expected_result5, expected_result6] and result_cost <= 13.5)

    def test_christofides3(self):
        # Given
        D3 = graph({'0': {'1': 120, '2': 270, '3': 100}, '1': {'0': 120, '2': 150, '3': 120},
                    '2': {'0': 270, '1': 150, '3': 250}, '3': {'0': 100, '1': 120, '2': 250}})
        expected_result1 = ['0', '3', '2', '1']
        expected_result2 = ['1', '0', '3', '2']
        expected_result3 = ['2', '1', '0', '3']
        expected_result4 = ['3', '2', '1', '0']
        expected_result5 = ['0', '1', '2', '3']
        expected_result6 = ['3', '0', '1', '2']
        expected_result7 = ['2', '3', '0', '1']
        expected_result8 = ['1', '2', '3', '0']
        expected_result9 = ['0', '2', '1', '3']
        expected_result10 = ['3', '0', '2', '1']
        expected_result11 = ['1', '3', '0', '2']
        expected_result12 = ['2', '1', '3', '0']
        expected_result13 = ['0', '3', '1', '2']
        expected_result14 = ['2', '0', '3', '1']
        expected_result15 = ['1', '2', '0', '3']
        expected_result16 = ['3', '1', '2', '0']

        # When
        result = christofides(D3)

        result_cost = 0
        for k in range(len(result) - 1):
            result_cost = result_cost + D3.G[result[k]][result[k + 1]]

        result_cost = result_cost + D3.G[result[0]][result[len(result) - 1]]

        # Then
        self.assertTrue(result in [expected_result1, expected_result2, expected_result3, expected_result4,
                                   expected_result5, expected_result6, expected_result7, expected_result8,
                                   expected_result9, expected_result10, expected_result11, expected_result12,
                                   expected_result13, expected_result14, expected_result15, expected_result16]
                        and result_cost <= 930)

    def test_christofides_4(self):
        # Given
        D4 = graph({'0': {'1': 2, '2': 270, '3': 1000}, '1': {'0': 2, '2': 15, '3': 120},
                    '2': {'0': 270, '1': 15, '3': 50}, '3': {'0': 1000, '1': 120, '2': 50}})
        expected = nx.approximation.traveling_salesman_problem(D4.to_nx(), cycle=False)

        # When
        result = christofides(D4)
        same_results = []
        for i in range(1, 5):
            same_results.append([result[(0 + i) % 4], result[(1 + i) % 4], result[(2 + i) % 4], result[(3 + i) % 4]])

        # Then
        self.assertTrue(expected in same_results)


if __name__ == '__main__':
    unittest.main()
