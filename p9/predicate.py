"""
Keishla D. Ortiz Lopez

CSCE 625 - Artificial Intelligence

P9: Goal regression for planning in the Blocksworld

Class Predicate
ex: on(a,c)
symbol = on
args = ['a','c']
"""

class Predicate(object):
    def __init__(self,symbol=None,args=[]):
        self._symbol = symbol
        self._args = args #can be empty

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value

    def __eq__(self, other):
        if isinstance(other, Predicate):
            return repr(self) == repr(other)
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result
        
    @property
    def args(self):
        return self._args

    def append(self,arg):
        if arg not in self._args:
            self._args.append(arg)
    
    """
    String representation of the predicate, ex: symbol = on, args = ['a','c'], then the string repr. is: on(a,c).
    """
    def __repr__(self):
        return self.symbol+"("+",".join(self.args)+")"

    