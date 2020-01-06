To implement the iterative DFS without using any auxiliary data structure
the information needed by the algorithm are stored in directly in the Vertex.
The algorithm works on the DFSGraph from Ex3.graph which extends te Graph class from 
TdP_collections by overraiding his internal Vertex class.
The new DFSGraph.Vertex class extends Graph.Vertex by adding the _visited and _visited_from
attributes and their related getters and setters.
At the end of the visit the algorithm reset the _visited and _visited_from attributes
to their default value to allow any subsequent visits.