from TdP_collections.graphs.graph import Graph

def iterative_dfs(graph, root):
    dictionary = {}

    dictionary[root] = None
    root.set_visited(True)

    node = root
    while True:
        if not node.is_visited():
            dictionary[node] = graph.get_edge(node.get_visited_from(), node)
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

    return dictionary