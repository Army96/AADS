from TdP_collections.graphs.graph import Graph
from TdP_collections.graphs.dfs import DFS
from Ex3.DFS import iterative_dfs
import random


def print_dictionary(dictionary):
    for vertex,edge in dictionary.items():
        print(f"{vertex} : {edge}")

# Generate graph
graph = Graph(False)
for i in range(0, 6):
    graph.insert_vertex(i)

for i in graph.vertices():
    for j in graph.vertices():
        if (i != j) and (graph.get_edge(j, i) is None) and random.getrandbits(1):
            graph.insert_edge(i, j, None)

vertices = []
for i in graph.vertices():
    vertices.append(i)

root = vertices[1]

recusive_dict = {}
recusive_dict[root] = None

DFS(graph, root, recusive_dict)
iterative_dict = iterative_dfs(graph, root)

print("recursive dfs: ")
print_dictionary(recusive_dict)
print("iterative dfs: ")
print_dictionary(iterative_dict)

