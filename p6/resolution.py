
"""
Keishla D. Ortiz Lopez
CSCE 625 - Artificial Intelligence

P6 - Propositional Theorem Prover using Resolution Refutation
Main program
"""
import sys
from clause import Clause
import heapq

"""
Method to parse the clauses in the file provided, ignores comments in the file (lines starting with '#'), empty lines
and similar clauses (i.e. same clauses, but with different order of literals)
"""
def parseClauses(clausesFile):
    clauses = []
    for line in open(clausesFile,'r'):
        if line.find("#") != -1 or not line.strip(): #ignore comments and empty lines
            continue
        newClause = Clause(line.split(),"input",len(clauses))
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
Method to check if a given literal (p) appears as a opposite literal in c
"""
def isSolvable(c,p):
    for p2 in c:
        if p2 == opposite(p):
            return True

    return False

"""
Implementation of the resolution pseudo-code
Data structure used: priority queue (heapq)
"""
def resolution():
    candidates = []
    
    for i in xrange(len(clauses)): #0 <= i < j < len(clauses)
        for j in xrange(i+1,len(clauses)):
            for p in clauses[i]:
                priority = min(len(clauses[i]),len(clauses[j])) #heuristic value
                if isSolvable(clauses[j],p): #a candidate
                    heapq.heappush(candidates,(priority,(i,j,prop(p))))
                    

    while len(candidates) != 0:
        resPair = heapq.heappop(candidates)[1]
        m = resolve(clauses[resPair[0]],clauses[resPair[1]],resPair[2])
        print "[Qsize={0}] resolving {1} and {2} on {3}: {4} and {5} -> {6}".format(len(candidates),resPair[0],resPair[1],resPair[2],clauses[resPair[0]],clauses[resPair[1]],m)
        if repr(m) == "()":
            print str(m.number)+": "+str(m)
            return m #success, return the empty clause, it is not necessary to add the empty clauses to clauses

        if not findClause(m,clauses):
            print str(m.number)+": "+str(m)
            for k in xrange(len(clauses)):
                for p in m:
                    priority = min(len(clauses[k]),len(m)) #heuristic value
                    a = k
                    b = m.number
                    if isSolvable(clauses[k],p): #a new candidate
                        heapq.heappush(candidates,(priority,(a,b,prop(p))))
            clauses.append(m) #add m to the list of clauses
        
    return None #failure

"""
Method to check if the given clause c is already in the list clauses
"""
def findClause(c,listClauses):
    for clause in listClauses:
        if repr(clause) == repr(c):
            return True
    return False

"""
Resolvent, removes the opposite literals of p and takes the union of the remaining literals
in c1 and c2 (excluding repeated literals).  Returns the new clause created.
"""
def resolve(c1,c2,p):
    literals = []

    for l in c1:
        if prop(l) != p and l not in literals:
            literals.append(l)

    for l in c2:
        if prop(l) != p and l not in literals:
            literals.append(l)

    newC = Clause(literals,[c1.number,c2.number],len(clauses))

    return newC

"""
Proof trace of the clause given
"""
def proof(clause,depth=0):
    print ''.ljust(depth)+str(clause.number)+": "+str(clause) + " " +str(clause.parent)
    if clause.parent == "input": #base case
        return

    proof(clauses[clause.parent[0]],depth+2)
    proof(clauses[clause.parent[1]],depth+2)

clausesFile = str(sys.argv[1])

clauses = parseClauses(clausesFile)
print "initial clauses: "
for c in clauses:
    print str(c.number)+": "+str(c)
print "-----------"

result = resolution()

if result is not None:
    print "success - empty clause!"
    print "--------------"
    print "proof trace:"
    proof(result)
else:
    print "failure - no empty clause found."