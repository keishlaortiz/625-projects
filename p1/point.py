"""
Keishla D. Ortiz-Lopez
CSCE 625: Artificial Intelligence
"""
class Point(object):

    """
    This class will contain just the id of a vertex along with its coordinates x and y.

    Properties:
    1. id: id of the vertex
    2. x: x coordinate
    3. y: y coordinate

    Methods:
    getters (methods with @property)
    1. __init__: constructor to initialize the point with the id and coordinates x and y.
    """

    def __init__(self,i,x,y):
        self._id = i
        self._x = x
        self._y = y

    @property
    def id(self):
        return self._id

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
