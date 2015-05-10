"""
Keishla D. Ortiz Lopez

CSCE 625 - Artificial Intelligence

P9: Goal regression for planning in the Blocksworld

Class Operator
"""

class Operator(object):
    def __init__(self,operator=None,precond=[],addList=[],delList=[],conflict=[]):
        self._operator = operator
        self._precond = precond
        self._addList = addList
        self._delList = delList
        self._conflict = conflict

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    
    @property
    def precond(self):
        return self._precond

    #may change or deleted
    def append(self,predicate,Type):
        if Type == 'p':
            if predicate not in self._precond:
                self._precond.append(predicate)
        elif Type == 'a':
            if predicate not in self._addlist:
                self._addList.append(predicate)
        elif Type == 'd':
            if predicate not in self._dellist:
                self._delList.append(predicate)
        elif Type == 'c':
            if predicate not in self._conflict:
                self._conflict.append(predicate)

    @property
    def addList(self):
        return self._addList
    
    @property
    def delList(self):
        return self._delList

    @property
    def conflict(self):
        return self._conflict
    

    
    