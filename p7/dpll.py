
"""
Keishla D. Ortiz Lopez
CSCE 625 - Artificial Intelligence

P7 - Propositional Satisfiability Solver (DPLL)
Main program

usage: python dpll.py fileName
"""
import sys
from clause import Clause
import copy

"""
Method to parse the clauses in the file provided, ignores comments in the file (lines starting with '#'), empty lines
and similar clauses (i.e. same clauses, but with different order of literals)
"""
def parseClauses(clausesFile):
    clauses = []
    for line in open(clausesFile,'r'):
        if line.find("#") != -1 or not line.strip(): #ignore comments and empty lines
            continue
        newClause = Clause(lits=line.split(),number=len(clauses))
        if not findClause(newClause,clauses): #ignore same clauses to make the search more efficient...
            clauses.append(newClause)

    return clauses

"""
Method to get the opposite of a literal:
ex: opposite(A) returns -A
"""
def opposite(lit):
    if lit[0] == "-":
        return lit[1:]
    return "-"+lit

"""
Method to get the proposition of a literal
ex: prop(-A) returns A
    prop(A) returns A
"""
def prop(lit):
    if lit[0] == "-": 
        return lit[1:]
    return lit

"""
Method to check if the given clause c is already in the list clauses
"""
def findClause(c,listClauses):
    for clause in listClauses:
        if repr(clause) == repr(c):
            return True
    return False

"""
Returns a list of sorted propositional symbols given a list of clauses
"""
def prop_symbols(listClauses):
    symbols = []

    for clause in listClauses:
        for l in clause:
            symbol = prop(l)
            if symbol not in symbols:
                symbols.append(symbol)

    return sorted(symbols)

"""
Pure symbol heuristic: Checks if one symbol in a list of symbols appears in the given list clauses with unknown truth values as pure (i.e. either as a positive literal
    or negative literal, and returns it with the respective value, True for positive and False for negative literal) that satisfies the clauses
    that symbol appears in.

    Returns None,None if there is no pure symbol in the given clauses
"""
def find_pure_symbol(symbols,clauses):
    for symbol in symbols:
        val_pos = 0
        val_neg = 0
        for c in clauses:
            if symbol in c:
                val_pos += 1
            if opposite(symbol) in c:
                val_neg += 1
        if val_pos != val_neg: #they cannot be equal
            value = None
            if val_pos == 0: #ex: symbol = A, and appears in all the clauses as -A
                value = False
            elif val_neg == 0: #ex: symbol = A and appears in all the clauses as A
                value = True

            if value is not None:
                print "pure_symbol on {0}={1}".format(symbol,value)
                return symbol,value
    return None,None

"""
Unit clause heuristic: finds a unit clause in the list clauses, i.e. a variable that is not in the model yet and
satisfies a clause (makes the clause true).  Note the function should take a list of clauses with unknown truth values
as find_pure_symbol heuristic.

Returns P,value (i.e. a unit clause P and a value True or False)
Returns None,None if there is no a unit clause
"""
def find_unit_clause(clauses,model):
    for c in clauses:
        P = None
        value = None

        for l in c:
            pr = prop(l)
            val = True

            if l[0] == "-":
                val = False

            if pr in model: #doesn't consider pr because it is already in the model
                continue

            elif P is not None: #there is more than 1 literal that are not in model yet, discard the symbol P and the rest of literals in this clause
                P = None
                value = None
                break

            else: #consider the symbol pr
                P = pr
                value = val

        if P is not None:
            print "unit_clause on {0} implies {1}={2}".format(c,P,value)
            return P, value

    return None,None

"""
Returns the first element of the list symbols
"""
def first(symbols):
    return symbols[0]

"""
Returns a list of symbols, except the fist one.
"""
def rest(symbols):
    return symbols[1:]

"""
Removes the element P from the list symbols and returns a new list without the symbol P.
"""
def remove(P,symbols):
    newSymbols = copy.deepcopy(symbols)
    newSymbols.remove(P)
    return newSymbols

"""
Assigns value (val) to the variable (var) in the dictionary model, and returns a copy of the model
with the new assignment.
"""
def assign(model,var,val,h=True):

    newModel = copy.deepcopy(model)

    newModel[var] = val

    char = 'T'
    if val == False:
        char = 'F'

    if not h:
        print "trying {0}={1}".format(var,char)

    return newModel

"""
Check if the given model satisfies the given clause.
This program assumes that all the clauses are disjunctions, so when the function finds a literal
that satisfies the clause (is True), returns True.  
Otherwise, there is a counter variable (literals) that keeps
track of the literals in the clause that appears in the model.  If the number of literals in clause doesn't match
the value in the variable counter literals, then returns None that means that the value of the clause is unknown.  
The last case is that the clause evaluates to False, in this case the method returns False.
"""
def eval(clause,model):
    #If one of the literal evaluates the clause as True, return True
    literals = 0
    for l in clause:
        p = prop(l)
        if p in model: #ex: prop(A) = A or prop(-A) = A
            literals += 1 #at least one literal in model is in the clause
            if p == l: #ex: l = A
                if model[p] == True:
                    return True
            else: #ex: l = -A
                if model[p] == False:
                    return True

    if literals != len(clause): #the value of the clause is unknown
        return None

    return False

"""
DPLL algorithm implementation
"""
def dpll_satisfiable(clauses):
    symbols = prop_symbols(clauses)

    print "props:"
    for symbol in symbols:
        print symbol,
    print ""

    print "initial clauses:"
    for c in clauses:
        print str(c.number)+": "+str(c)
    print "-----------"

    return dpll(clauses,symbols,{})

def dpll(clauses,symbols,model):
    global COUNTER
    COUNTER += 1
    rest_clauses = [] #contains the clauses with unknown values, used in both heuristics
    print "model= {0}".format(model)
    for c in clauses:
        value = eval(c,model) #returns True, False or None
        if value == False: #if one of the clauses is false in model, return False (backtracking)
            print "backtracking"
            return False
        if value != True: #we don't know the value of the clause yet, so append the clause in rest_clauses
            rest_clauses.append(c)

    if len(rest_clauses) == 0 and len(symbols) == 0: #every clause in clauses is true in model and there is no more symbols without values, print solution
        print "nodes searched={0}".format(COUNTER)
        print "solution:"

        for var,val in sorted(model.items()):
            print "{0}={1}".format(var,val)
        print "-----------"
        print "true props:"
        for var,val in sorted(model.items()):
            if val:
                print var
        return True 

    #pure symbol heuristic
    #pass to the function the list rest_clauses: clauses with unknown values
    P,value = find_pure_symbol(symbols,rest_clauses)
    if P is not None:
        return dpll(clauses,remove(P,symbols),assign(model,P,value))

    #unit clause heuristic
    #pass to the function the list rest_clauses: clauses with unknown values
    P,value = find_unit_clause(rest_clauses,model)
    if P is not None:
        return dpll(clauses,remove(P,symbols),assign(model,P,value))

    #no heuristic
    P = first(symbols)
    rest_symbols = rest(symbols)
    return (dpll(clauses,rest_symbols,assign(model,P,True,False)) or dpll(clauses,rest_symbols,assign(model,P,False,False)))

COUNTER = 0
clausesFile = str(sys.argv[1])
clauses = parseClauses(clausesFile)

result = dpll_satisfiable(clauses)

if not result:
    print "No solution found for this problem."