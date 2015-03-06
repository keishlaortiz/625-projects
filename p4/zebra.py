"""
    Zebra puzzle class for the backtracking search function
    Variables: men (nationality), colors, snacks, pets and drinks
    Domain: numbers from 0 to 4 (i.e. houses labeled by integers where 0 is the first house and 4 is the last house)
"""
class Zebra(object):
    def __init__(self,mrv=False):
        self.mrv = mrv
        self.men = ["Englishman","Spaniard","Norwegian","Ukranian","Japanese"]
        self.colors = ["red","green","ivory","yellow","blue"]
        self.snacks = ["Hershey","Kit Kat","Smarties","Snicker","Milky Way"]
        self.drinks = ["water","oj","tea","coffee","milk"]
        self.pets = ["dog","zebra","snails","fox","horse"]

        self._variables = self.men[:]+self.colors[:]+self.snacks[:]+self.drinks[:]+self.pets[:]

        self.define_domains()

        self.count = 0 #used in the backtracking function to count the number of states searched

    def getType(self,v):

        if v in self.colors:
            return "Color"
        if v in self.snacks:
            return "Snack"
        if v in self.drinks:
            return "Drink"
        if v in self.pets:
            return "Pet"
        

        return "Nationality"

    def __repr__(self):
        return "zebra"

    @property
    def variables(self):
        return self._variables

    @property
    def domains(self):
        return self._domains
    
    def define_domains(self):
        self._domains = {}
        for var in self.variables:
            self._domains[var] = range(5) #0 to 4 (houses labeled by integers)

    def consistency(self,a,b,assignment):
        Type = self.getType(a) #variable type
        def baseConstraints():
            if a in ("Englishman","Ukranian","Japanese","Spaniard","tea","red","blue","dog","Milky Way","ivory","green","milk","coffee") and b == 0:
                return False

            if a in ("Englishman","red","yellow","green","ivory","milk","Kit Kat","coffee","Norwegian") and b == 1:
                return False

            if a in ("coffee","tea","water","oj","green","Ukranian","Snicker","Norwegian") and b == 2:
                return False

            if a in ("Norwegian","blue","milk") and b in (3,4):
                return False

            return True
        #restrict houses to 1 color, man, drink, snack and pet
        def assignedValue():
            for var in self.variables:
                if var in assignment:
                    if assignment[var] == b and self.getType(var) == Type:
                        return True
            return False

        def sameHouse():
            if a == "Englishman":
                if "red" in assignment:
                    if assignment["red"] != b:
                        return False

            if a == "red":
                if "Englishman" in assignment:
                    if assignment["Englishman"] != b:
                        return False

            if a == "Spaniard":
                if "dog" in assignment:
                    if assignment["dog"] != b:
                        return False

            if a == "dog":
                if "Spaniard" in assignment:
                    if assignment["Spaniard"] != b:
                        return False

            if a == "Kit Kat":
                if "yellow" in assignment:
                    if assignment["yellow"] != b:
                        return False

            if a == "yellow":
                if "Kit Kat" in assignment:
                    if assignment["Kit Kat"] != b:
                        return False

            if a == "Smarties":
                if "snails" in assignment:
                    if assignment["snails"] != b:
                        return False

            if a == "snails":
                if "Smarties" in assignment:
                    if assignment["Smarties"] != b:
                        return False

            if a == "Snicker":
                if "oj" in assignment:
                    if assignment["oj"] != b:
                        return False

            if a == "oj":
                if "Snicker" in assignment:
                    if assignment["Snicker"] != b:
                        return False

            if a == "Ukranian":
                if "tea" in assignment:
                    if assignment["tea"] != b:
                        return False
            if a == "tea":
                if "Ukranian" in assignment:
                    if assignment["Ukranian"] != b:
                        return False

            if a == "Japanese":
                if "Milky Way" in assignment:
                    if assignment["Milky Way"] != b:
                        return False
            if a == "Milky Way":
                if "Japanese" in assignment:
                    if assignment["Japanese"] != b:
                        return False

            if a == "coffee":
                if "green" in assignment:
                    if assignment["green"] != b:
                        return False
            if a == "green":
                if "coffee" in assignment:
                    if assignment["coffee"] != b:
                        return False
            return True

        def isNeighbor():
            if a == "green":
                if "ivory" in assignment:
                    if assignment["ivory"] != (b - 1):
                        return False

            if a == "ivory":
                if "green" in assignment:
                    if assignment["green"] != (b + 1):
                        return False

            if a == "Hershey":
                if "fox" in assignment:
                    c = assignment["fox"]
                    if abs(b - c) != 1:
                        return False

            if a == "fox":
                if "Hershey" in assignment:
                    c = assignment["Hershey"]
                    if abs(b - c) != 1:
                        return False

            if a == "Kit Kat":
                if "horse" in assignment:
                    c = assignment["horse"]
                    if abs(b-c) != 1:
                        return False

            if a == "horse":
                if "Kit Kat" in assignment:
                    c = assignment["Kit Kat"]
                    if abs(b-c) != 1:
                        return False
            return True

        if not baseConstraints():
            return False

        if not sameHouse():
            return False
        
        if not isNeighbor():
            return False

        if assignedValue():
            return False


        return True

    def assign(self,var,val,assignment):
        assignment[var] = val

    def unassign(self,var,val,assignment):
        if var in assignment:
            del assignment[var]

    def goal_test(self,assignment):
        return len(assignment) == len(self.variables)