
from node import *
class Problem(object):
    def __init__(self,initial,goal=None):
        self._initial = initial #node
        self._goal = goal #node
        if goal is None:
            self.generate_goal()

    """
    Compares the string representation of block with the goal's block
    """
    def goal_test(self,block):
        return repr(block) == repr(self.goal.block)

    @property
    def initial(self):
        return self._initial

    @initial.setter
    def initial(self, value):
        self._initial = value
    
    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, value):
        self._goal = value
    
    """
    Generates the goal state for the problem using the number of stacks and blocks
    """
    def generate_goal(self):
        goal_state = []
        characters = map(chr, range(65,65+self.initial.block.blocks))

        for i in xrange(self.initial.block.stacks):
            if i == 0:
                goal_state.append(characters)
            else:
                goal_state.append([])

        self.goal = Node(Block(self.initial.block.stacks,self.initial.block.blocks,goal_state,False))
