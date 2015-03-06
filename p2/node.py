"""
Keishla D. Ortiz-Lopez
CSCE 625: Artificial Intelligence
"""
import copy
from block import *
class Node(object):
    """
    
    """

    def __init__(self,s,p=None,d=0,h=0):
        self._s = s #Block
        self._parent = p #blocksworld state parent
        self._depth = d #integer
        self._heur = h #floating-point number
        self._neighbors = [] #a list of Nodes

    @property
    def block(self):
        return self._s
    """
    Generates successors for the node
    """
    @property
    def successors(self):
        topElements = {}
        tempBlock = copy.deepcopy(self.block)

        #get top block of each stack
        for i in xrange(self.block.stacks):
            if len(self.block.state[i]) == 0:
                continue
            topElements[i] = tempBlock.state[i].pop()

        #place top blocks in other stacks
        for key,value in topElements.items():
            for i in xrange(self.block.stacks):
                if key != i: #avoid to place the block in its original stack
                    new_block = copy.deepcopy(self.block)
                    new_block.state[key].pop()
                    new_block.state[i].append(value)
                    self._neighbors.append(Node(new_block))

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