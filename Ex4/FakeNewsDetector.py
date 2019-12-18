from TdP_collections.graphs.graph import Graph

""" 
For each vertex decide if it is better to install the sofwtware on the node (cost of install_yes) or 
on his children (cost of install_no).
3 funtion, by caching results every function is executed only once per node, complexity: O(3n) = O(n)
"""

def install(graph, root, parent=None, cache = {}, installed_list = []):
    """
    Install the software on the minimum number of vertices so that for every pair of vertices,
    at least one of them has the software.

    Return a 2 elements tuple composed by the number of vertices on which the software is 
    installed and a list of such vertices
    """
    if root in cache:
        if "install" in cache[root]:
            return cache[root]["install"]
    else:
        cache[root] = {}

    install_cost = install_yes(graph, root, parent, cache, installed_list)
    not_install_cost = install_no(graph, root, parent, cache, installed_list)

    if install_cost <= not_install_cost:
        installed_list.append(root)
        cache[root]["install"] = (install_cost, installed_list)
    else:
        cache[root]["install"] = (not_install_cost, installed_list)

    return cache[root]["install"]

def install_yes(graph, root, parent, cache, installed_list):
    """ Return the cost of installing the software on the root vertex"""
    if root in cache:
        if "yes" in cache[root]:
            return cache[root]["yes"]
    
    cache[root]["yes"] = 1 + sum(install(graph, children, root, cache, installed_list)[0] for children in children(graph, root, parent))
    return cache[root]["yes"]

def install_no(graph, root, parent, cache, installed_list):
    """ Return the cost of installing the software on the children of root"""
    if root in cache:
        if "no" in cache[root]:
            return cache[root]["no"]
    
    cache[root]["no"] = sum(install_yes(graph, children, root, cache, installed_list) for children in children(graph, root, parent))
    return cache[root]["no"]

def children(graph, root, parent):
    """ 
    Return an iterator on the children of root,
    a children is defined as every neighbour except parent
    """
    for edge in graph.incident_edges(root):
        opposite_vertex = edge.opposite(root)
        if opposite_vertex != parent:
            yield opposite_vertex