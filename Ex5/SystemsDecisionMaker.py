def systems_decision_maker(graph) -> dict:
    """Initially we consider that all the vertices have the system.
    full_coverage is true if all the vertices adjacent to him have the system.
    At the beginning everyone has it, therefore we set it a true.
    full_coverage_degree represents the number of friends who have the full_coverage parameter set to true.
    Therefore, at the beginning, the full_coverage_degree is equal to degree"""
    for v in graph.vertices():
        v.set_system(True)
        v.set_full_coverage(True)
        v.set_full_coverage_degree(graph.degree(v))

    """I check all the vertices of the graph"""
    for v in graph.vertices():

        """If the vertex and all of his friends have the system, the vertex is one of the candidates which doesn't have 
        the system.
        Else we go to the next vertex"""
        if v.system() & v.full_coverage():

            """We search the vertex with full_coverage set to true and with the minimum full_coverage_degree.
            We take the smaller than full_coverage_degree instead of a degree because so, when we remove a system from a
            computer, we minimize the number of computers that will not be able to remove the system."""
            minimum = v
            for e in graph.incident_edges(v):
                u = e.opposite(v)
                if u.full_coverage() and (minimum.full_coverage_degree() > u.full_coverage_degree()):
                    minimum = u

            """We remove the system from the vertex "minimum" and we set the full_coverage parameter of all his friends 
            to False"""
            minimum.set_system(False)
            for e in graph.incident_edges(minimum):
                u = e.opposite(minimum)
                """If the full_coverage parameter was True, we set it to False and we decrement the full_coverage_degree
                of its friends"""
                if u.full_coverage():
                    u.set_full_coverage(False)
                    for edge in graph.incident_edges(u):
                        vertex = edge.opposite(u)
                        vertex.set_full_coverage_degree(vertex.full_coverage_degree() - 1)

    return graph










