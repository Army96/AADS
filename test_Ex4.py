from TdP_collections.graphs.graph import Graph
from Ex4 import FakeNewsDetector

graph = Graph()

vertices = []
for i in range(0, 9):
    vertices.append(graph.insert_vertex(i))

graph.insert_edge(vertices[0], vertices[1])
graph.insert_edge(vertices[0], vertices[2])
graph.insert_edge(vertices[0], vertices[3])
graph.insert_edge(vertices[1], vertices[4])
graph.insert_edge(vertices[1], vertices[5])
graph.insert_edge(vertices[2], vertices[6])
graph.insert_edge(vertices[3], vertices[7])
graph.insert_edge(vertices[5], vertices[8])


n,l = FakeNewsDetector.installer(graph, vertices[0])
print(n)
print(*l, sep="-")
