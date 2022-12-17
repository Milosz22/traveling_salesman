from Christofides.graph import *
import copy


def is_path(G, a, b):
    ''' true if there is a path from a to b in G else false, bfss'''
    visited = []
    q = []
    visited.append(a)
    q.append(a)
    while len(q) != 0:
        s = q.pop()
        if s == b:
            return True
        for neighbour in list(G[s].keys()):
            if neighbour not in visited:
                visited.append(neighbour)
                q.append(neighbour)
    return False


def add_edge_cycle(G, a, b):
    '''G- undirected tree (dictionary), a,b - vertices in G
    returns true if after we add an edge {a,b}, there is a cycle in G + {a,b}'''
    if b in G[a]:
        return False
    if is_path(G, a, b):
        return True
    return False


def find_min_weight(G):
    '''G is an undirected graph (dict) nontrival
    returns [a,b] where {a,b} is an edge with minimal weight'''

    # assign m any weight
    m = -1
    for v in G:
        if G[v] != {}:  # i need a vertice that has an edge

            k = list(G[v].keys())[0]
            m = G[v][k]
            a = v
            b = k
            break
    if m == -1:
        return False

    for v in G:
        if G[v] != {}:
            k = min(G[v], key=G[v].get)
            if G[v][k] < m:
                m = G[v][k]
                a = v
                b = k

    return [a, b, m]


def kruskal(Gr):
    '''Gr is an undirected graph (class graph) that is connected
    returns minimal spanning tree'''
    # i create a graph with no edges
    graf = graph(copy.deepcopy(Gr.G))
    T = {}
    for v in graf.G:
        T[v] = {}
    counter = 0
    while counter < len(T) - 1:
        [c, d, value] = find_min_weight(graf.G)
        if not add_edge_cycle(T, c, d):
            T[c][d] = value
            T[d][c] = value
            counter += 1
        del graf.G[c][d]
        del graf.G[d][c]

    return T
