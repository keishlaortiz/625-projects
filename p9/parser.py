"""
Keishla D. Ortiz Lopez
CSCE 625 - Artificial Intelligence

P9: Goal regression for planning in the Blocksworld

Class Parser

Parses the files of operators and initial state (initial facts)
"""

from operator2 import Operator
from predicate import *
import copy

class Parser(object):

    def __init__(self,opFile,initFile):
        self._opFile = opFile
        self._initFile = initFile

    #Done
    def parseOperatorsFile(self):

        operators = []
        file = open(self.operatorsFile,'r')
        lines = file.readlines()

        for x in xrange(len(lines)):
            line = lines[x]
            if line.find('#') != -1 or not line.strip() or line.find("OPER") == -1:
                continue

            line = line.strip().split()[1][:-1].split('(')
            symbol = line[0]
            args = line[1].split(',')
            operator = Predicate(symbol,args)

            precond = []
            addList = []
            delList = []
            conflict = []

            for i in xrange(x+1,x+5):
                lines[i] = lines[i].strip()
                list = lines[i].split(':')

                facts = list[1].strip().split()
                predicates = []

                for fact in facts:
                    fact = fact[:-1].split('(')
                    symbol = fact[0]
                    args = fact[1].split(',')
                    predicate = Predicate(symbol,args)
                    predicates.append(predicate)

                #print predicates
                if list[0] == "precond":
                    precond = copy.deepcopy(predicates)
                elif list[0] == "addlist":
                    addList = copy.deepcopy(predicates)
                elif list[0] == "dellist":
                    delList = copy.deepcopy(predicates)
                elif list[0] == "conflict":
                    conflict = copy.deepcopy(predicates)

            oper = Operator(operator,precond,addList,delList,conflict)

            operators.append(oper)
        
        file.close()
        return operators

    #Done
    def parseInitFile(self):
        initFacts = []

        for line in open(self.initFile,'r'):
            if line.find('#') != -1 or not line.strip():
                continue

            line = line.strip()[:-1].split('(')
            symbol = line[0]
            args = line[1].split(',')

            initFacts.append(Predicate(symbol,args))

        return initFacts

    @property
    def operatorsFile(self):
        return self._opFile

    @property
    def initFile(self):
        return self._initFile
