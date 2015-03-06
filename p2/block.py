"""
Keishla D. Ortiz-Lopez
CSCE 625: Artificial Intelligence
"""
import random
class Block(object):

    def __init__(self,s,b,state=None,random_state=True):
        self._stacks = s
        self._blocks = b
        self._state = state
        if random_state: #generate a random state
            self.generate_state()

    @property
    def state(self):
        return self._state

    """A unique string representation of the block's state. Method very useful for the astar function."""
    def __repr__(self):
        s = '#'
        for stack in self.state:
            s += ''.join(stack) + '#'
        return s
        
    @state.setter
    def state(self, new_state):
        self._state = new_state

    @property
    def stacks(self):
        return self._stacks

    @stacks.setter
    def stacks(self, s):
        self._stacks = s

    @property
    def blocks(self):
        return self._blocks

    @blocks.setter
    def blocks(self, b):
        self._blocks = b
    
    """
    Generates a random state
    """
    def generate_state(self):
        characters = map(chr, range(65,65+self.blocks))
        self.state = []

        for i in xrange(self.stacks):
            self.state.append([])
        
        random.shuffle(characters)
        i = 0
        while i != self.blocks:
            for c in xrange(0,self.stacks):
                divisor = random.randint(1,self.blocks-1)
                number = random.randint(0,int(self.blocks/divisor))
                a = 0
                while a < number and i < self.blocks:
                    self.state[c].append(characters[i])
                    i += 1
                    a += 1

