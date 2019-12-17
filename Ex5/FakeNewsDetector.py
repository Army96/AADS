from Ex5.graph import Graph
from Ex5.SystemsDecisionMaker import systems_decision_maker
from Ex5.GraphGenerator import graphs_generator

graphs = graphs_generator(False)
update_graph = {}
i = 0
for graph in graphs.values():
    update_graph[i] = systems_decision_maker(graph)
    j = 0
    for v in update_graph[i].vertices():
        if v.system():
            j += 1
    i += 1
    print("In the ", i, "-th graph there are ", j, " user with the system on their pc")