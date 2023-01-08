from Algorithm.kruskal import kruskal
from Algorithm.christofides import christofides
from Algorithm.graph import *
import sys

'''The function loads a graph from a file and saves it to a global variable graph_example.
I adopt the convention according to which the graph in the file is written in the form of m lines, and in each
line 3 numbers a, b, v separated by a space. m is the number of edges of graph, a and b are vertices, and v
is the weight of the edges between them.'''

def load_graph_from_file(filepath):
    D = {}  # this will be the graph we load
    file = filepath

    with open(file) as f:
        for line in f.readlines():
            a = line[0]
            b = line[2]
            v = line[4]
            if a not in D:
                D[a] = {}
            D[a][b] = int(v)
    global graph_example
    graph_example = D

    return graph_example

def load_graph_from_file_coordinates(filepath):
    D = []  # this will be the graph we load
    file = filepath
    i = 0
    with open(file) as f:
        for line in f.readlines():
            D.append([])
            if line[1] != ' ':
                helper = "".join([line[0], line[1]])
                D[i].append(int(helper))
                indeks_y = 3
            else:
                D[i].append(int(line[0]))
                indeks_y = 2

            if line[indeks_y + 1] != '\n':
                helper = "".join([line[indeks_y], line[indeks_y + 1]])
                D[i].append(int(helper))
            else:
                D[i].append(int(line[indeks_y]))
            i = i + 1

    global graph_example_1
    graph_example_1 = D

    return graph_example_1


'''The function takes a graph from the global variable graph_example, calls kruskal on it 
and saves the result to a file. The format of the saved data is the same as in the input file'''


def save_kruskal_graph_to_file():
    file = "example_out.txt"
    my_graph = kruskal(graph(graph_example, coordinates=1))
    vertices = my_graph.items()

    f = open(file, "w")  # "w" means that if the file did not exist it will create it, if it exists it will overwrite it
    for v in vertices:
        edges = v[1].items()
        for e in edges:
            line = ' '.join([v[0], e[0], e[1]]) # v[0] - wierzchołek startowy; e[0] - wierzchołek docelowy; e[1] - waga
            f.write(line)
            f.write("\n")

    f.close()

    return


def save_christo_graph_to_file(graph_to_save, filepath):
    file = filepath
    hamilton = christofides(graph(graph_to_save, coordinates=1))

    f = open(file, "w")  # "w" means that if the file did not exist it will create it, if it exists it will overwrite it
    for v in hamilton:
        line =str(v)
        f.write(line)
        f.write("\n")

    f.close()

    return


def end_app():
    sys.exit()