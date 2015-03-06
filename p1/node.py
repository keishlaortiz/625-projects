"""
Keishla D. Ortiz-Lopez
CSCE 625: Artificial Intelligence
"""
class Node(object):
    """
    Properties of class Node:
    (see methods with @property)
    1. location: Point object with vertex id and coordinates x and y.
    2. parent: Node object that helps to find a path in the reversed order
    3. depth: the depth of the Node
    4. heur: the heuristic value of the Node
    5. successors: a list of Nodes that contains nodes reachable from the Node

    Methods:
    NOTE: Methods with @property are getters and methods with @property_name.setter are setters
    1. __init__: constructor used to initialize the properties of the Node.
    2. add_neighbor: add a node w to the successors lists only if w is not in the list.
    """

    def __init__(self,v,p=None,d=0,h=0):
        self._v = v #Point
        self._parent = p #Node
        self._depth = d #integer
        self._heur = h #floating-point number
        self._neighbors = [] #a list of Nodes

    @property
    def location(self):
        return self._v
        
    @property
    def successors(self):
        return self._neighbors

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self,u):
        self._parent = u

    @property
    def depth(self):
        return self._depth

    @depth.setter
    def depth(self,d):
        self._depth = d

    @property
    def heur(self):
        return self._heur

    @heur.setter
    def heur(self,h):
        self._heur = h

    def add_neighbor(self,w):
        if w not in self._neighbors:
            self._neighbors.append(w)
