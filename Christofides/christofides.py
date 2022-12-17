from Christofides.kruskal import *
from Christofides.graph import *
import networkx as nx


def odd_deg_vertices(G):
    '''Returns a list of odd-degree vertices of G'''

    degs = list(nx.degree(G.to_nx()))
    n = len(degs)
    G_odd = list()

    for j in range(n):
        if degs[j][1] % 2 != 0:
            G_odd.append(degs[j][0])

    return G_odd


def ham_from_eul(E):
    '''Returns vertices of a Hamiltonian cycle made from
    consecutive varying vertices of an Eulerian cycle E'''

    vertices = [u for u, v in E]
    H = list()
    m = len(vertices)

    for j in range(m):
        if vertices[j] not in H:
            H.append(vertices[j])

    return H


def christofides(G):
    '''Returns vertices of a Hamiltonian cycle with the cost lower or equal
     to 1.5 of the cost of the optimal Hamiltonian cycle in graph G'''

    if nx.edges(nx.complete_graph(nx.nodes(G.to_nx()))) != nx.edges(G.to_nx()):
        raise Exception("graph G is not complete")

    if len(list(nx.nodes(G.to_nx()))) < 3:
        raise Exception("G has not enough vertices")

    # minimum spanning tree
    MST = graph(kruskal(G))
    # odd-degree vertices of MST
    MST_odd = odd_deg_vertices(MST)

    # subgraph of G induced by odd-degree vertices of MST
    G_odd = nx.subgraph(G.to_nx(), MST_odd)
    # minimum-weight perfect matching of G_odd
    M = nx.Graph()
    M.add_edges_from(nx.min_weight_matching(G_odd))

    # multigraph made from edges of MST and M
    multi_MST = nx.MultiGraph()
    multi_MST.add_edges_from(nx.edges(MST.to_nx()))

    multi_M = nx.MultiGraph()
    multi_M.add_edges_from(M.edges())

    multi_MST.update(edges=multi_M.edges())

    multigraph = multi_MST

    # Eulerian cycle in multigraph (starting in '0' vertex)
    E = nx.eulerian_circuit(multigraph, source='0')

    # Hamiltonian cycle made from consecutive varying vertices of E
    H = ham_from_eul(E)

    return H
