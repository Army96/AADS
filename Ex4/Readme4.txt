Exercise 4

Given an undirected graph G=(V,E) find a minimum-cardinality set S of vertices that contains at least one endpoint of every edge.
This problem is extremely unlikely to have a polynomial time algorithm (even for planar graphs), but is polynomially solvable on trees using dynamic programming.

Subproblem:	for each v∈V & y∈{YES, NO, MAYBE}: size of the smallest vertex cover S in the subtree rooted at v such that [v∈S]

Guess: 		Does MAYBE=YES or NO?

Recurrence:	V(v,Maybe)	min{ V(v,Yes), V(v,No) }			O(1)
		V(v,Yes)	1 + sum{ V(c,Maybe) for each children c of v}	#children(v)
		V(v,No)		sum{ V(c,Maybe) for each children c of v}	#children(v)

DP Time:	#subproblems ⋅ time/subproblems = 3 ⋅ #numchildren(v) = O(V)

Original problem: V(root, MAYBE)

The algorithm, given a graph and its chosen root, returns a 2 elements tuple composed by the number of vertices on which the software is installed and a list of such vertices.
The algorithm starts from the root and then continues deciding vertex by vertex if it is the case to install the software or not, by computing the cost of the 2 cases.
The decision taken will be saved into a helper memory (cache:dict in the code) and in the case the decision was to install, that vertex will be added also in the list of the vertex with the software (installed_list:list in the code) and the number of vertex increased. 
After that the algorithm repeats the same operation on all the children (thanks to, the helper method children that will return an iterator of all the neighbors except the parent) of the previous node and checks in the helper memory if that vertex has already been computed, in that case it won’t revaluate the costs.
When there won’t be any other vertexes the code will stop.