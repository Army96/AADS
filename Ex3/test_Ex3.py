from graph import Graph
import DFS
import random

# Generate random graph
print("Generating random graph..")
graph = Graph()
for i in range(0, 6):
    graph.insert_vertex(i)

for i in graph.vertices():
    for j in graph.vertices():
        if (i != j) and (graph.get_edge(j, i) is None) and random.getrandbits(1):
            graph.insert_edge(i, j, None)

print("Vertices:")
for v in graph.vertices():
    print(v)

print("Edges:")
for e in graph.edges():
    print(e)

for root in graph.vertices():
    print(f"\nIterative DFS from vertex: {root}")
    print("\nVertex\t:\tVisited from edge")
    for vertex,edge in DFS.iterative_dfs(graph, root).items():
        print(f"{vertex}\t:\t{edge}")