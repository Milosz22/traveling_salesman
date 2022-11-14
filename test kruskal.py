import unittest
import kruskal
from graph import *

E = (graph([[0,1],[1,0]]).G)
F = (graph([[0,1,0,0],[1,0,1,1],[0,1,0,0],[0,1,0,0]]).G)
H = (graph([[0,1,0,0],[1,0,1,0],[0,1,0,0],[0,0,0,0]]).G)
K = (graph([[0,0,0],[0,0,0],[0,0,0]]).G)
G1 = (graph({'0':{'1':0.1, '2':0.2}, '1':{'0':0.1}, '2':{'0':0.2}}).G)
G2 = (graph({'0':{'1':3.2}, '1':{'1':3.2}, '2':{}}).G)




class MyTestCase(unittest.TestCase):

# I'm testing the "is_path" function. 

    def test_is_path_1(self):
        result = kruskal.is_path(F, 1, 2)
        self.assertEqual(True, result)

    def test_is_path_2(self):
        result = kruskal.is_path(F, 0, 1)
        self.assertEqual(True, result)

    def test_is_path_3(self):
        result = kruskal.is_path(H, 0, 3)
        self.assertEqual(False, result)

    def test_is_path_4(self):
        result = kruskal.is_path(E, 0, 0)
        self.assertEqual(True, result)

    def test_is_path_5(self):
        result = kruskal.is_path(K, 1, 2)
        self.assertEqual(False, result)

    def test_is_path_6(self):
        result = kruskal.is_path(K, 0, 10)
        self.assertEqual(False, result)

# I'm testing the "add_edge_cycle" function.

    def test_add_edge_cycle_1(self):
        result = kruskal.add_edge_cycle(F, 0, 1)
        self.assertEqual(False, result)

    def test_add_edge_cycle_2(self):
        result = kruskal.add_edge_cycle(H, 0, 1)
        self.assertEqual(False, result)

    def test_add_edge_cycle_3(self):
        result = kruskal.add_edge_cycle(F, 2, 3)
        self.assertEqual(True, result)

    def test_add_edge_cycle_4(self):
        result = kruskal.add_edge_cycle(H, 2, 3)
        self.assertEqual(False, result)

    def test_add_edge_cycle_5(self):
        result = kruskal.add_edge_cycle(K, 1, 2)
        self.assertEqual(False, result)

    def test_add_edge_cycle_6(self):
        result = kruskal.add_edge_cycle(K, 0, 4)
        self.assertEqual(False, result)

# I'm testing the "find_min_weight" function.
    def test_find_min_weight_1(self):

        #Given
        G1 = (graph({'0': {'1': 0.1, '2': 0.2}, '1': {'0': 0.1}, '2': {'0': 0.2}}).G)
        expected_result= ['0', '1', 0.1]
        #When
        result = kruskal.find_min_weight(G1)

        #Then
        self.assertEqual(expected_result, result)


        # self.assertEqual(['0', '1', 0.1], result)


       # result = kruskal.find_min_weight(G1)
       # self.assertEqual(['0', '1', 0.1], result)

    def test_find_min_weight_2(self):
       result = kruskal.find_min_weight(G2)
       self.assertEqual(['0', '1', 3.2], result)

# I'm testing the "kruskal" function.



if __name__ == '__kruskal__':
        unittest.kruskal()
