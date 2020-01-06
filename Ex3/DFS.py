from Ex3.graph import DFSGraph

def iterative_dfs(graph, root) -> dict:
    """
    Perform iterative DFS of the undiscovered portion of Graph graph starting at Vertex rot.

    :param Graph graph: The Graph on wich perform DFS
    :param Graph.Vertex vertex: The starting vertex of the DFS
    :return: a result_dictionary mapping each vertex to the edge that was used to discover it.
    :rtype: dict
    """

    if not isinstance(graph, DFSGraph):
        raise TypeError('graph must be DFSGraph')
    if not isinstance(root, DFSGraph.Vertex):
        raise TypeError('root must be a DFSGraph.Vertex')

    result_dictionary = {}

    result_dictionary[root] = None
    root.set_visited(True)
    node = root
    
    while True:
        if not node.is_visited():
            result_dictionary[node] = graph.get_edge(node.get_visited_from(), node)
            node.set_visited(True)

        # cicle edges to find the first not visited neighbour vertex
        next_node = None
        for edge in graph.incident_edges(node):
            opposite = edge.opposite(node)
            if not opposite.is_visited():
                next_node = opposite
                break
        
        if next_node is None:    # No other edges to visit
            if node == root:     # exit if in root
                break
            else:                # Go back to previous node
                node = node.get_visited_from()
        else:                    # Set next edge to visit
            next_node.set_visited_from(node)
            node = next_node

    # reset status
    for v in graph.vertices():
        v.set_visited(False)
        v.set_visited_from(None)

    return result_dictionary