"""
Jobs Puzzle class for the backtracking search function

Variables: people
Domain: jobs
"""
class Jobs(object):

    def __init__(self,mrv=False):
        self.people = ["Roberta","Thelma","Steve","Pete"] 
        self.jobs = ["chef","guard","nurse","clerk","police officer","teacher","actor","boxer"] 
        self.define_domains()
        self.mrv = mrv
        self.count = 0

    def __repr__(self):
        return "jobs"

    def consistency(self,a,b,assignment): #a = variable, b = value, assignment might be empty...
        def baseConstraints():
            if a in ("Roberta","Thelma") and b in ("actor","nurse","clerk"): #jobs hold by a male
                return False
            if a == "Roberta" and b in ("boxer","chef","police officer"): 
                return False 
            if a == "Thelma" and b == "police officer": #Thelma is the chef, so she cannot be the police officer
                return False
            if a == "Pete" and b in ("nurse","teacher","police officer","chef"):
                return False
            if a == "Steve" and b == "chef": #chef is a female
                return False
            return True

        def valueAssigned():
            for x in self.variables:
                try:
                    if b in assignment[x]:
                        return True
                except Exception:
                    break

            return False

        if not baseConstraints():
            return False

        if len(assignment) != 0:
            maximum = 2

            if valueAssigned():
                return False

            if a in assignment: 
                if b in assignment[a]: #avoid duplications
                    return False
                if len(assignment[a]) == maximum: #restric to two jobs
                    return False

        return True

    @property
    def variables(self):
        return self.people

    @property
    def domains(self):
        return self._domains
    
    def define_domains(self):
        self._domains = {}
        for people in self.people:
            self._domains[people] = self.jobs

    def assign(self,var,value,assignment):
        if var not in assignment:
            assignment[var] = []

        assignment[var].append(value)
    

    def goal_test(self,assignment):
        flag = False
        if len(assignment) == len(self.variables):
            for var in self.variables:
                try:
                    if len(assignment[var]) == 2:
                        flag = True
                    else:
                        flag = False
                        break
                except Exception:
                    flag = False
                    break
        
        return flag

    def unassign(self,var,value,assignment):
        if var in assignment:
            if value in assignment[var]:
                assignment[var].remove(value)
        