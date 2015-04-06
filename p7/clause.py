"""
Keishla D. Ortiz Lopez
CSCE 625 - Artificial Intelligence

P7 - Propositional Satisfiability Solver (DPLL)

Clause class, it contains the literals of a clause, the parent(s), and number (i.e. the index number).

The most important method in this class is the __repr__ method that returns a string representation
of the clause, which is useful to compare clauses and print the clause

"""
class Clause(object):
    def __init__(self,lits=[],parent=None,number=0):
        self._literals = lits
        self._parent = parent
        self._number = number

    def __len__(self):
        return len(self.literals)

    def __iter__(self):
        return iter(self.literals)

    #returns literals in order, this is useful to avoid duplicated clauses in different order
    @property
    def literals(self):
        return sorted(self._literals)

    @property
    def number(self):
        return self._number

    @property
    def parent(self):
        return self._parent
    
    #string representation of the clause, useful to check if two clauses are equal and print it
    def __repr__(self):
        mClause = "("
        if len(self.literals) >= 1:
            for c in self.literals:
                mClause += c +" v "

            mClause = mClause[:-3]

        mClause += ")"
        return mClause
    