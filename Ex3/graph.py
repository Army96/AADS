from TdP_collections.graphs.graph import Graph

class DFSGraph(Graph):
  """
  Extended Graph lass whit custom Vertex to support iterative 
  DFS without support datasructure.
  """

  #------------------------- nested Vertex class -------------------------
  class Vertex(Graph.Vertex):
    """
    Extended Vertex to support iterative 
    DFS without support datasructure.
    """

    __slots__ = ['_visited', '_visited_from']

    def __init__(self, x):
      """Do not call constructor directly. Use Graph's insert_vertex(x)."""
      
      super().__init__(x)
      self._visited = False
      self._visited_from = None
      
    def set_visited(self, visited):
      self._visited = visited
    
    def is_visited(self):
      return self._visited
    
    def set_visited_from(self, vertex):
      self._visited_from = vertex

    def get_visited_from(self):
      return self._visited_from