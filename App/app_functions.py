from Algorithm.kruskal import kruskal
from Algorithm.christofides import christofides
from Algorithm.graph import *
import networkx
import matplotlib.pyplot as plt
import random
import sys

'''The function loads a graph from a file and saves it to a global variable graph_example.
I adopt the convention according to which the graph in the file is written in the form of m lines, and in each
line 3 numbers a, b, v separated by a space. m is the number of edges of graph, a and b are vertices, and v
is the weight of the edges between them.'''

main_map_graph = {}

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

            if len(line)-1 > indeks_y:
                if line[indeks_y + 1] != '\n':
                    helper = "".join([line[indeks_y], line[indeks_y + 1]])
                    D[i].append(int(helper))
                else:
                    D[i].append(int(line[indeks_y]))
            else:
                D[i].append(int(line[indeks_y]))
            i = i + 1

    global graph_example_1
    graph_example_1 = D
    global main_map_graph
    main_map_graph = graph(D, coordinates=1)

    return graph_example_1

def load_coordinates(filepath):
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

            if len(line)-1 > indeks_y:
                if line[indeks_y + 1] != '\n':
                    helper = "".join([line[indeks_y], line[indeks_y + 1]])
                    D[i].append(int(helper))
                else:
                    D[i].append(int(line[indeks_y]))
            else:
                D[i].append(int(line[indeks_y]))
            i = i + 1
    return D
'''The function takes a graph from the global variable graph_example, calls kruskal on it 
and saves the result to a file. The format of the saved data is the same as in the input file'''


# def save_kruskal_graph_to_file():
#     file = "example_out.txt"
#     my_graph = kruskal(graph(graph_example, coordinates=1))
#     vertices = my_graph.items()
#
#     f = open(file, "w")  # "w" means that if the file did not exist it will create it, if it exists it will overwrite it
#     for v in vertices:
#         edges = v[1].items()
#         for e in edges:
#             line = ' '.join([v[0], e[0], e[1]])
#             f.write(line)
#             f.write("\n")
#
#     f.close()
#
#     return


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


def draw(L):

    G = graph(L, coordinates=1)
    H=christofides(G)
    Gnx = nx.Graph()
    i = 0
    for [a, b] in L:
        Gnx.add_node(str(i), pos=(a, b))
        i += 1
    for i in range(len(H)-1):
        Gnx.add_edge(H[i],H[i+1])
    Gnx.add_edge(H[0], H[-1])
    color=[]
    c=0
    for node in Gnx:
        if c==0:
            color.append('red')
            c=1
        else:
            color.append('yellow')
    nx.draw(Gnx, nx.get_node_attributes(Gnx, 'pos'), with_labels=True, node_size=300,node_color=color)
    pos = nx.spring_layout(Gnx)
    for node, (x, y) in pos.items():
        plt.text(x, y, node, fontsize=0.5, ha='center', va='center')
    plt.show()
#draw([[random.randint(1, 50), random.randint(1, 50)] for i in range(15)])
def draw_graph():
    x = load_coordinates("generate_graph_2.txt")
    w = []
    with open("adress.txt") as f:
        for line in f.readlines():
            v = ''.join(line)
            if v[-1] == '\n':
                w.append(v[0:-1])
            else:
                w.append(v)
    r = []
    with open("customer_result.txt") as f:
        for line in f.readlines():
            r.append(''.join(line[0:-1]))

    Gnx = nx.Graph()
    i = 0
    for i in range(len(r)):
        Gnx.add_node(r[i], pos=(x[i][0], x[i][1]))
        i += 1
    for i in range(len(r) - 1):
        Gnx.add_edge(r[i], r[i + 1])
    Gnx.add_edge(r[0], r[-1])
    color=[]
    c=0
    for node in r:
        if c==0:
            color.append('red')
            c=1
        else:
            color.append('yellow')
    nx.draw(Gnx, nx.get_node_attributes(Gnx, 'pos'), with_labels=True, node_size=300,node_color=color)
    pos = nx.spring_layout(Gnx)
    for node, (x, y) in pos.items():
        plt.text(x, y, node, fontsize=0.5, ha='center', va='center')
    plt.show()



# For this function to work properly you must first call load_graph_from_file function
# in order to use global variable main_map_graph.
def load_client_vertices_and_save_to_file(client_graph_filepath):
    CL = []  # We will read customer vertices to this list
    file = client_graph_filepath
    with open(file) as f:
        for line in f.readlines():
            CL.append(line)
            CL[len(CL) - 1] = CL[len(CL) - 1].strip()  # Delete '\n' at the end of every line

    # Check if CL contains correct veritces for our graph
    CL_int = [int(x) for x in CL]
    min_CL = min(CL_int)
    max_CL = max(CL_int)
    if min_CL < 0 or max_CL >= len(main_map_graph.G):
        print("Wrong vertice in customer list!")
        return

    CD = {}  # Customer graph in form of dictionary

    for v in main_map_graph.G:
        if v in CL:
            CD[v] = {}
            for v2 in main_map_graph.G[v]:
                if v2 in CL:
                    CD[v].update({v2: main_map_graph.G[v][v2]})

    save_christo_graph_to_file(CD, "customer_result.txt")





def end_app():
    sys.exit()