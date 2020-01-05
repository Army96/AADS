from Ex5.SystemsDecisionMaker import systems_decision_maker
from Ex5.GraphGenerator import graphs_generator

"""A collection of 100 graphs"""
graphs = graphs_generator(False)
"""The updated 100 graps"""
update_graph = {}
i = 0
"""A variable used to calculate the average number of pc with the system"""
sum = 0
"""A variable used to count the number of error. It must be 0 at the end"""
error = 0
for graph in graphs.values():
    update_graph[i] = systems_decision_maker(graph)
    """Count the number of pc with the system"""
    j = 0
    for v in update_graph[i].vertices():
        if v.system():
            j += 1
        """Check if there is an error. An error occurs when both the system and full_coverage are false or true
        in a vertex. In the first case because that vertex should have the system, 
        in the second because it should not have it"""
        if (not v.full_coverage() and not v.system()) or (v.full_coverage() and v.system()):
            print("ERRORE")
            error += 1
    i += 1
    sum += j
    print("In the ", i, "-th graph there are ", j, " user with the system on their pc")
average = sum/100
print("The average pc with the system are ", average)
print("error ", error)