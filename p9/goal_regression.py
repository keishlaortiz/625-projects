"""
Keishla D. Ortiz Lopez
CSCE 625 - Artificial Intelligence

P9: Goal regression for planning in the Blocksworld

Main program

usage: python goal_regression.py OPERATORS_FILE INITIAL_STATE_FILE
"""

from parser import *
from queue import *
import sys

#list1 U list2
def union(list1,list2):
    list = copy.deepcopy(list1)
    for item in list2:
        if item not in list:
            list.append(item)
    return list

#list1 \ list2
def difference(list1,list2):
    list = []
    for item in list1:
        if item not in list2 and item not in list:
            list.append(item)
    return list

#list1 /\ list2
def intersection(list1,list2):
    list = []

    for item in list1:
        if item in list2 and item not in list:
            list.append(item)

    return list

#(goals \ oper.addList) U oper.precond
def regress(goals,oper):
    
    #goals \ oper.addList
    newgoals = difference(goals,oper.addList)
    #newgoals U oper.preconds
    newgoals = union(newgoals,oper.precond)

    return newgoals

"""
Goal regression function
"""
def goal_regression(goals,opers,kb):
    queue = Queue()
    queue.push(Node(goals))
    visited = {}
    count = 1

    while True:
        print "iter={0}, queue={1}".format(count,len(queue))
        item = queue.pop()
        if len(intersection(item.goals,kb)) == len(item.goals): #all goals satisfied by kb
            print "solution found!"
            return item.plan

        print "context: {0}".format(item.plan)
        print "goal stack: {0}".format(item.goals)

        for goal in item.goals:
            for oper in opers:
                if len(intersection(item.goals,oper.addList)) != 0:
                    if len(intersection(item.goals,union(oper.delList,oper.conflict))) == 0:
                        newgoals = regress(item.goals,oper)
                        newplan = copy.deepcopy(item.plan)
                        newplan.append(oper.operator)
                        if repr(newplan) not in visited:
                            print "considering using {0} to achieve {1}".format(repr(oper.operator),repr(goal))
                            visited[repr(newplan)] = 1
                            queue.push(Node(newgoals,newplan))
        count+=1

"""Main function """
def main():
    OP_FILE = str(sys.argv[1])
    INIT_FILE = str(sys.argv[2])

    parser = Parser(OP_FILE,INIT_FILE)

    operators = parser.parseOperatorsFile()
    kb = parser.parseInitFile()

    while True:
        command = raw_input()  
        if command == "quit": 
            break
        #otherwise is a list of goals
        predicates = command.split()
        goals = []

        for goal in predicates:
            goal = goal[:-1].split('(')
            symbol = goal[0]
            args = goal[1].split(',')
            fact = Predicate(symbol,args)
            goals.append(fact)

        #call function goal_regression 
        plan = goal_regression(goals,operators,kb)
        print "plan:"
        for pl in plan:
            print pl

        command = ""

if __name__ == '__main__':
    main()
        

