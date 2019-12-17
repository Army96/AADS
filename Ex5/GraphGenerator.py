from Ex5.graph import Graph
import random
import pickle

"""
Return a dictionary with 100 graphs. Graphs are directed if "directed" is set to True.
Complexity O(n^3).
"""

def graphs_generator(directed) -> dict:
    graphs = {}
    n = 100
    # create 100 graphs
    for i in range(0, n):
        graphs[i] = Graph(directed)
    # insert 100 vertices in every graph
    for graph in graphs.values():
        for i in range(0, 100):
            graph.insert_vertex(i)
    # insert edges among the vertices of every graph
    for graph in graphs.values():
        for i in graph.vertices():
            for j in graph.vertices():
                if (i == j) or (graph.get_edge(i, j) is not None and not directed): #controllare condizione
                    pass
                else:
                    if random.getrandbits(1):
                        graph.insert_edge(i, j, None)

    return graphs