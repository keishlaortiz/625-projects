"""
Keishla D. Ortiz-Lopez
CSCE 625: Artificial Intelligence
"""

from node import *
from point import *

class Parser(object):
    """
    This class is to parse the graph file.

    Property:
    1. _file: a string with the name of input file to be read

    Methods:
    1. __init__: constructor to initialize the property _file
    2. parseFile: method that reads _file (the graph file) and return a list of nodes of the graph.
    """

    def __init__(self,inputFile):
        self._file = inputFile

    def parseFile(self):
        vertices = 0
        edges = 0
        i = 0
        nodes = [] #all the nodes of the graph (list of Nodes)

        for line in open(self._file,'r'):

            #get number of vertices
            if line.find("vertices:") != -1:
                vertices = int(line.split(': ')[1])
                
            #get number of edges 
            elif line.find("edges:") != -1:
                edges = int(line.split(': ')[1])
                
            #process vertices
            elif i <= vertices:
                values = line.split(' ')
                vertex = Point(int(values[0]),int(values[1]),int(values[2]))
                node = Node(vertex)
                nodes.append(node)

            #process edges
            else:
                values = line.split(' ')
                v1 = int(values[1])
                v2 = int(values[2])

                #the graph is undirected, so v1->v2 and v2->v1 is the same.
                #note that the id of the vertex is also an index in the list to the same node.
                #I guess that any graph file provided to the program should work if the format is the same.
                nodes[v1].add_neighbor(nodes[v2])
                nodes[v2].add_neighbor(nodes[v1])


            i += 1

        print "vertices={0}, edges={1}".format(vertices,edges)

        return nodes