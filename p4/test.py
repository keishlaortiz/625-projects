from jobs import *
import sys
from collections import defaultdict
from zebra import *

sys.setrecursionlimit(100000)

def order_domain_values(var,assignment,csp):
    domain = csp.domains[var][:]

    return domain

"""
Useful for the MRV, counts the number of invalid values for each variable
"""
def values(u_vars,csp,assignment):
    count_values = defaultdict(lambda:0)

    for var in u_vars:
        for val in csp.domains[var]:
            if not csp.consistency(var,val,assignment):
                count_values[var] += 1

    return count_values

"""
Returns the variable with the maximum number of invalid values
"""
def get_maximum(dictionary):
    maximum = -1
    key = ""
    for v in dictionary:
        if dictionary[v] > maximum:
            maximum = dictionary[v]
            key = v

    return key

def select_unassigned_variable(assignment,csp):
    if csp.mrv:
        if repr(csp) == "jobs":
            u_vars = [v for v in csp.variables if v not in assignment or len(assignment[v]) != 2]
        else:
            u_vars = [v for v in csp.variables if v not in assignment]
        count_values = values(u_vars,csp,assignment)
        if len(count_values) != 0:
            return get_maximum(count_values)

    else:
        if repr(csp) == "jobs":
            for v in csp.variables:
                if v not in assignment or len(assignment[v]) != 2:
                    return v
        else:
            for v in csp.variables:
                if v not in assignment:
                    return v

"""
Recursive backtracking
"""
def backtrack(assignment,csp):
    if csp.goal_test(assignment):
        return assignment

    var = select_unassigned_variable(assignment,csp)

    for val in order_domain_values(var,assignment,csp):
        csp.count += 1
        if csp.consistency(var,val,assignment):
            csp.assign(var,val,assignment)
            result = backtrack(assignment,csp)
            if result is not None:
                return result
        csp.unassign(var,val,assignment)

    return None

"""
Backtracking search function 
"""
def backtracking_search(csp):
    return backtrack({},csp)

"""
Prints the solution of the backtracking search function
"""
def print_solution(csp,solution):
    print "==============================="
    if repr(csp) == "jobs":
        print "Solution of Jobs Puzzle\n"
        for var in sorted(solution):
            print "Person: {0}".format(var)
            print "Jobs: {0} and {1}".format(solution[var][0],solution[var][1])
            print "---------"
        
    else:
        h_num_z = -1
        color_z = ""
        h_num_w = -1
        color_w = ""
        print "Solution of Zebra Puzzle\n"
        for h in range(5):
            print "House: {0}".format(h+1)
            for (var, val) in sorted(solution.items()):
                if var == "zebra":
                    h_num_z = val
                elif var == "water":
                    h_num_w = val
                if var in csp.colors:
                    if val == h_num_z:
                        color_z = var
                    elif val == h_num_w:
                        color_w = var
                if val == h:
                    Type = csp.getType(var)
                    print "{0} = {1} |".format(Type,var),
            print ""
        print ""
        print "Where does the zebra live? In the {0} house".format(color_z)
        print "Which house do they drink water? In the {0} house".format(color_w)

    print ""
    print "Number of states searched:"
    s = ""
    if not csp.mrv:
        s = "No "
    print "{1}MRV = {0}".format(csp.count,s)

sys.stdout = open("output.txt","w")
job = Jobs()
job1 = Jobs(True)
result1 = backtracking_search(job)
result2 = backtracking_search(job1)

#Solutions of Jobs Puzzle and Zebra Puzzle with and without MRV
print_solution(job,result1)
print_solution(job1,result2)

zebra = Zebra()
zebra1 = Zebra(True)

result3 = backtracking_search(zebra)
result4 = backtracking_search(zebra1)

print_solution(zebra,result3)
print_solution(zebra1,result4)