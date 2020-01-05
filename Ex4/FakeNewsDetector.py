from TdP_collections.graphs.graph import Graph

"""
For each vertex decide if it is better to install the sofwtware on this vertex (cost of install_yes) or 
on all his children (cost of install_no).
3 funtion, by caching results every function is executed only once per vertex, complexity: O(3n) = O(n)
"""

def installer(graph :Graph, root :Graph.Vertex):
    """
    Install the software on the minimum number of vertices so that for every pair of vertices,
    at least one of them has the software.

    Return a 2 elements tuple composed by the number of vertices on which the software is 
    installed and a list of such vertices
    """

    if not graph.degree(root):    # Base Case single vertex tree
        return(1, [root])

    # Start iteration 
    return install(graph, root, None, {}, [])


def install(graph :Graph, root :Graph.Vertex, parent :Graph.Vertex, cache :dict, installed_list :list):
    """
    NOTE: Use installer(graph, root) to start installation.
    Decide whether to install the software on the root vertex or on all his children
    Return a 2 elements tuple composed by the number of vertices on which the software is 
    installed and a list of such vertices
    """

    # if thefuncion was alredy called on this vertex return the results from the cache
    if root in cache and "install" in cache[root]:
            return cache[root]["install"]
    else:   # initializzze cache for this vertex
        cache[root] = {}

    # calculate costs
    install_cost = install_yes(graph, root, parent, cache, installed_list)
    not_install_cost = install_no(graph, root, parent, cache, installed_list)

    if install_cost <= not_install_cost:    # install the software and put the results in cache
        installed_list.append(root)
        cache[root]["install"] = (install_cost, installed_list)
    else:   # not install and put the results in cache
        cache[root]["install"] = (not_install_cost, installed_list)

    return cache[root]["install"]


def install_yes(graph :Graph, root :Graph.Vertex, parent :Graph.Vertex, cache :dict, installed_list :list):
    """ Return the cost of installing the software on the root vertex"""

    # If thefuncion was alredy called on this vertex return the results from the cache
    if root in cache and "yes" in cache[root]:
            return cache[root]["yes"]
    
    cache[root]["yes"] = 1 + sum(install(graph, children, root, cache, installed_list)[0] for children in children(graph, root, parent))
    return cache[root]["yes"]

def install_no(graph :Graph, root :Graph.Vertex, parent :Graph.Vertex, cache :dict, installed_list :list):
    """ Return the cost of installing the software on the children of root"""
    
    # If thefuncion was alredy called on this vertex return the results from the cache
    if root in cache and "no" in cache[root]:
            return cache[root]["no"]
    
    cache[root]["no"] = sum(install_yes(graph, children, root, cache, installed_list) for children in children(graph, root, parent))
    return cache[root]["no"]




def children(graph :Graph, root :Graph.Vertex, parent :Graph.Vertex):
    """ 
    Helper function.
    Return an iterator on the children of root,
    a children is defined as every neighbour except the vertex passed as parent
    """
    for edge in graph.incident_edges(root):
        opposite_vertex = edge.opposite(root)
        if opposite_vertex != parent:
            yield opposite_vertex