from __future__ import division
from problem import *
import pqueue as pq
import sys
from math import *

"""
h1: Counts the number of blocks out of place (i.e. incorrect position).  
"""
def heuristic1(node):
    incorrect_place = 0
    if repr(node.block) == repr(problem.goal.block): #goal state, return -1
        return -1

    for x in range(problem.goal.block.blocks):
        try:
            if node.block.state[0][x] != problem.goal.block.state[0][x]:
                incorrect_place += 1
        except IndexError:
            incorrect_place += (node.block.blocks - len(node.block.state[0]))
            break
        
    return incorrect_place

"""
h2: Logic based on the discussion from: http://www.d.umn.edu/~kvanhorn/cs2511/discussions/heuristics.html
"""
def heuristic2(node):
    if repr(node.block) == repr(problem.goal.block): #goal state, return -1
        return -1

    h1 = node.block.blocks - len(node.block.state[0])

    h2 = 0
    for x in range(problem.goal.block.blocks):
        try:
            if node.block.state[0][x] != problem.goal.block.state[0][x]:
                h2 += 1
        except IndexError:
            break
    
    c = 0
    flag = True
    block_id = '@'
    for x in range(problem.goal.block.blocks):
        try:
            if node.block.state[0][x] == problem.goal.block.state[0][x]:
                c += 1
                block_id = node.block.state[0][x] #get last block
            else: #just count the first c blocks in the correct positions (ex... A,B,C,E...blocks; c=3)
                flag = False #means that I cannot place a block in the top
                break
        except IndexError: #if first stack is empty flag will be true
            break

    h3 = node.block.blocks - c
    
    h = h1+h2+h3
    if flag: #means that I can place a block in the top of the first stack (if possible; I need to check each stack)
        for x in range(node.block.stacks):
            if x != 0 and len(node.block.state[x]) != 0:
                if chr(ord(block_id) + 1) == node.block.state[x][-1]: #means that top block can be placed on the first stack
                    h -= 1 #do this once because the goal is to have all the blocks in the first stack
                    break
                
    return h

"""
Implementation of the A* search algorithm.
"""
def astar_search(problem,function):
    frontier = pq.queue()
    frontier_sizes = []
        
    if function == 'h1':
        problem.initial.heur = heuristic1(problem.initial)
    else:
        problem.initial.heur = heuristic2(problem.initial)

    pq.enqueue(frontier,problem.initial.heur,problem.initial)
    g = {}
    g[repr(problem.initial.block)]=0
    visited = []
    i = 1

    while pq.size(frontier) != 0 and i <= UPPER_BOUND:
        f,node = pq.dequeue(frontier)
        frontier_sizes.append(pq.size(frontier))
        #print "iter={0}, queue={1}, f=g+h={2}, depth={3}".format(i,pq.size(frontier),f,node.depth)

        if problem.goal_test(node.block):
            return (node,i,max(frontier_sizes)+1)

        visited.append(repr(node.block))
        children = node.successors

        for ch in children:
            if repr(ch.block) in visited: #ignore nodes in the list visited, just look on those nodes that are already in frontier or not
                continue 
            depth = node.depth + 1
            if repr(ch.block) not in g or depth < g[repr(ch.block)]:
                ch.depth = depth
                g[repr(ch.block)] = depth
                if function == 'h1':
                    ch.heur = heuristic1(ch)
                else:
                    ch.heur = heuristic2(ch)

                priority = depth + ch.heur
                ch.parent = node
                try:
                    pq.update(frontier,priority,ch) #update the priority of the node in frontier
                except KeyError: #means that is not in the frontier, enqueue the node...
                    pq.enqueue(frontier,priority,ch)
                
        i += 1
    return (None,i,max(frontier_sizes)+1)

"""
Print the path or steps.
"""
def print_path(node):
    i = node
    path = []
    while i != None:
        path.append(i.block)
        i = i.parent
    print "solution path:"
    for p in reversed(path):
        for x in range(p.stacks):
            print "{0} |  {1}".format(x+1,"   ".join(p.state[x]))
        print ""

UPPER_BOUND = 20000
SOLUTIONS = 1 
#sys.stdout = open("transcript2.txt","w")
function = str(sys.argv[4]).lower()
target = open(str(sys.argv[3]), 'w')
s = int(sys.argv[1])
b = int(sys.argv[2])

if s > 2 and b > 1 and (function == 'h1' or function == 'h2'):
        n = 0
        su = 0
        f = 0
        sum_depth = 0
        sum_goal = 0
        max_size = 0
        line1 = "Stacks: " + str(sys.argv[1]) + " Blocks: "+str(sys.argv[2])
        target.write(line1)
        target.write("\n")
        #Random state given the number of stacks and the number of blocks
        while n < SOLUTIONS:
                initial_state = Block(s,b)
                initial_node = Node(initial_state)

                problem = Problem(initial_node)
                print "==========================="
                print "initial state:"
        
                for x in range(initial_state.stacks):
                        print "{0} |  {1}".format(x+1,"   ".join(initial_state.state[x]))

                result = astar_search(problem,function)
        
                if result[0] is not None:
                        print "success! heuristic = {0}, depth={1}, total_goal_tests={2}, max_queue_size={3}".format(function,result[0].depth,result[1],result[2])
                        print_path(result[0])
                        su += 1
                        sum_depth += result[0].depth
                        sum_goal += result[1]
                        max_size += result[2]
                        
                else: 
                        if result[1] < 20000:
                                print "There is no solution for this particular problem. Try again."
                        else:
                                f += 1
                                print "The function reached the upper bound of the goal tests. Thus, the behavior of the heuristic function is not efficient for this problem."
                n += 1
        try:
            average_depth = round(sum_depth/su,1)
            average_tests = round(sum_goal/su,1)
            average_size = round(max_size/su,1)
        except Exception:
            average_depth = 0
            average_tests = 0
            average_size = 0
        target.write("Heuristic function = "+function+"\n")
        target.write("Depth = "+str(average_depth)+"\n")
        target.write("Goal tests = "+str(average_tests)+"\n")
        target.write("Max Size = "+str(average_size)+"\n")
        target.write("Number of problems with more than 20000 goal tests = "+str(f)+"/"+str(SOLUTIONS))
else:
        print "Program cannot solve the blocksworld problem with {0} stacks and/or {1} blocks; or the heuristic function {2} doesn't exist. Try again.".format(s,b,function)

target.close()



