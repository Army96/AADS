from Ex5.graph import Graph
from Ex5.SystemsDecisionMaker import systems_decision_maker


"""Creation of a small graph used to test the SystemDecisionMaker"""
graph = Graph(False)

for i in range(0, 10):
    graph.insert_vertex(i)

for i in graph.vertices():
    for j in graph.vertices():

        if i.element() == 0 and (j.element() == 1 or j.element() == 2):
            graph.insert_edge(i, j)

        if i.element() == 1 and (j.element() == 2 or j.element() == 3):
            graph.insert_edge(i, j)

        if i.element() == 2 and (j.element() == 3 or j.element() == 7):
            graph.insert_edge(i, j)

        if i.element() == 3 and (j.element() == 4 or j.element() == 5 or j.element() == 7 or j.element() == 8):
            graph.insert_edge(i, j)

        if i.element() == 4 and (j.element() == 5 or j.element() == 6):
            graph.insert_edge(i, j)

        if i.element() == 5 and (j.element() == 6 or j.element() == 7):
            graph.insert_edge(i, j)

        if i.element() == 6 and (j.element() == 7 or j.element() == 8 or j.element() == 9):
            graph.insert_edge(i, j)

        if i.element() == 7 and j.element() == 8:
            graph.insert_edge(i, j)

        if i.element() == 8 and j.element() == 9:
            graph.insert_edge(i, j)

update_graph = systems_decision_maker(graph)

error = 0
i = 0
for v in update_graph.vertices():
    if v.system():
        i += 1
    """Check if there is an error. An error occurs when both the system and full_coverage are false or true
    in a vertex. In the first case because that vertex should have the system, 
    in the second because it should not have it"""
    if (not v.full_coverage() and not v.system()) or (v.full_coverage() and v.system()):
        print("ERROR")
        error += 1

print("Computer with the system in the graph:", i)
print("Error in the graph", error)