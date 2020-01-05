graph.py
In the graph structure have been added three new parameter compared to the course data structure: system, full_coverage
and full_coverage_degree, with their getter and setter method (system(), full_coverage(), full_coverage_degree(),
set_system(boolean), set_full_coverage(boolean), set_full_coverage_degree(int)).
•	system: this parameter is a boolean that indicates if the computer must have or must not have the system
•	full_coverage: this parameter is a boolean that it’s true if all the neighbors of the computer have the system
•	full_coverage_degree: this parameter is a integer that represent the number of the friends of the vertex with the
    full_coverage parameter set to true

GraphGenerator.py
This file contains the graphs_generator() function that return a dictionary with 100 graphs. Graphs are directed if
"directed" is set to True.

SystemDecisionMaker.py
SystemsDecisionMaker.py is the Python file which contains the function that decides which computers must have the system
and which must not have it. The function name is systems_decision_maker(graph) and it requires as input a graph, that
structure is implemented in the graph.py file inserted in this exercise folder. The system_decision_maker output is an
updated graph in which the “system” parameter is set to true if the computer must have the system, else it is set to false.

FakeNewsDetector.py
FakeNewsDetector.py contains the main of this exercise. It uses the GraphGenerator.py to create the 100 undirected graphs
and then it uses the SystemDecisionMaker.py to decide which computers must have the system. After, we count how many
computers have the system in each graph, we calculate the average and how many error are present (always 0 in all the test).
To check the correctness of the code, we checked if there are no vertices with both the "system" and "full_coverage"
parameters set to true or false. In fact, if both are set to true, it means that this vertex should not have the system,
while, if both are set to false, it means that both this vertex and one of his friends don’t have the system, of
consequently there is a couple of friends without the system.

Test.py
In this file we create a small graph of 10 vertex and we checked if the SystemDecisionMaker returns a correct and an
optimal solution. In this case the solution is optimal, but in the randomly generated graphs no.