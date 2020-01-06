To implement the iterative DFS without using any auxiliary data structure
the information needed by the algorithm are stored in directly in the Vertex.
The algorithm works on the DFSGraph from Ex3.graph which extends te Graph class from 
TdP_collections by overraiding his internal Vertex class.
The new DFSGraph.Vertex class extends Graph.Vertex by adding the _visited and _visited_from
attributes and their related getters and setters.
At the end of the visit the algorithm reset the _visited and _visited_from attributes
to their default value to allow any subsequent visits.

The time complexity is the same as the stack based DFS, O(n+m) where n=number of vetex and
m = number of edges, but without using additional memory for the auxiliary data structure
since the space for the inforamtion needed to the visit is alredy allocated in the graph.

The test script "test_Ex3.py" generate 2 random graph, one directed and one undirected, and
print the results of the visit executed starting from every vertices of the graph.
The results are in the form of a dictionary where every visited vertex is associated with
the edge used to visit it.