#!/usr/bin/env python3

from Ex3.graph import DFSGraph as Graph
from Ex3.DFS import iterative_dfs
import random

def random_graph_generator(vertices_number, directed=False):
    """
    Generate a random graph of vertices_number vertices, 
    the graph is directed if directed is True or undirected (default) otherwhise
    """
    graph = Graph(directed)
    for i in range(0, vertices_number):
        graph.insert_vertex(i)

    for i in graph.vertices():
        for j in graph.vertices():
            if random.getrandbits(1):
                try:
                    graph.insert_edge(i, j, None)
                except:
                    pass
    
    return graph

def complete_iterative_DFS(graph):
    print("\nVertices:", end=" ")
    print(*graph.vertices(), sep=",")

    print("\nEdges:")
    print(*graph.edges(), sep="\n")

    for root in graph.vertices():
        print(f"\nIterative DFS from vertex: {root}")
        print("\nVertex\t:\tVisited from edge")
        for vertex,edge in iterative_dfs(graph, root).items():
            print(f"{vertex}\t:\t{edge}")


# Generate random graph
print("Generating random undirected graphs ..")
graph = random_graph_generator(10)
complete_iterative_DFS(graph)

print("\nGenerating random directed graphs ..")
graph = random_graph_generator(10, directed=True)
complete_iterative_DFS(graph)