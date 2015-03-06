#!/usr/bin/python
"""
Keishla D. Ortiz-Lopez
CSCE 625: Artificial Intelligence
"""

import sys
from parser import *
from collections import deque
from math import *
import heapq

"""
Method to find a node given the coordinates x and y, return the respective node or None if there is no
node with those coordinates.
"""
def findNode(x,y):
    for node in nodes:
        if node.location.x == x and node.location.y == y:
            return node
    return None

"""
Calculates the distance between two points, useful for the GBFS function.
"""
def distance(p1,p2):

    return round(sqrt(pow(p2.x-p1.x,2)+pow(p2.y-p1.y,2)),2)

"""
Breadth-first search
"""
def BFS(i_state,g_state):
    frontier = deque()
    visited_nodes = []
    frontier_sizes = []
    frontier.append(i_state)
    i = 1
    m = 1
    while len(frontier) != 0:
        node = frontier.popleft() #equivalent to "dequeue"
        frontier_sizes.append(len(frontier))
        #print "iter={0}, frontier={1}, popped={2} ({3},{4}), depth={5}, dist2goal={6}".format(i,len(frontier),node.location.id,node.location.x,node.location.y,node.depth,distance(node.location,g_state.location))
        if node.location.id == g_state.location.id:
            return (True,i,max(frontier_sizes)+1,m)
        visited_nodes.append(node.location.id)
        children = node.successors
        for ch in children:
            if ch not in frontier and ch.location.id not in visited_nodes:
                m += 1
                #set properties here
                nodes[ch.location.id].depth = node.depth + 1
                nodes[ch.location.id].parent = node.location.id
                frontier.append(nodes[ch.location.id])
                #print "pushed {0} ({1},{2})".format(ch.location.id,ch.location.x,ch.location.y)

        i += 1

    return (False,0,0,0)

"""
Depth-first search
"""
def DFS(i_state,g_state):
    frontier = deque() 
    visited_nodes = []
    frontier_sizes = []
    frontier.append(i_state)
    i = 1
    m = 1
    while len(frontier) != 0:
        node = frontier.pop() #stack's pop operation
        frontier_sizes.append(len(frontier))
        #print "iter={0}, frontier={1}, popped={2} ({3},{4}), depth={5}, dist2goal={6}".format(i,len(frontier),node.location.id,node.location.x,node.location.y,node.depth,distance(node.location,g_state.location))
        if node.location.id == g_state.location.id:
            return (True,i,max(frontier_sizes)+1,m)
        visited_nodes.append(node.location.id)
        children = node.successors
        for ch in children:
            if ch not in frontier and ch.location.id not in visited_nodes:
                m += 1
                #set properties here
                nodes[ch.location.id].depth = node.depth + 1
                nodes[ch.location.id].parent = node.location.id
                frontier.append(nodes[ch.location.id])
                #print "pushed {0} ({1},{2})".format(ch.location.id,ch.location.x,ch.location.y)
        i += 1

    return (False,0,0,0)
"""
Greedy Best First Search
"""
def GBFS(i_state,g_state):
    frontier = []
    visited_nodes = []
    frontier_sizes = []
    h = distance(i_state.location,g_state.location)
    nodes[i_state.location.id].heur = h
    i_state.heur = h
    heapq.heappush(frontier,(h,i_state))
    i = 1
    m = 1
    while len(frontier) != 0:
        node = heapq.heappop(frontier)[1]
        frontier_sizes.append(len(frontier))
        #print "iter={0}, frontier={1}, popped={2} ({3},{4}), depth={5}, dist2goal={6}".format(i,len(frontier),node.location.id,node.location.x,node.location.y,node.depth,node.heur)
        if node.location.id == g_state.location.id:
            return (True,i,max(frontier_sizes)+1,m)
        visited_nodes.append(node.location.id)
        children = node.successors
        for ch in children:
            heur = distance(ch.location,g_state.location)
            if (heur,ch) not in frontier and ch.location.id not in visited_nodes:
                m += 1
                #set properties here
                nodes[ch.location.id].depth = node.depth + 1
                nodes[ch.location.id].parent = node.location.id
                nodes[ch.location.id].heur = heur
                heapq.heappush(frontier,(nodes[ch.location.id].heur,nodes[ch.location.id]))
                #print "pushed {0} ({1},{2})".format(ch.location.id,ch.location.x,ch.location.y)
            else: #keep track of the shortest path, just affects the number of iterations and path length in some cases
                if nodes[ch.location.id].depth > node.depth + 1: #if depth of ch is greater than node.depth plus one, then change it to be node.depth + 1
                    nodes[ch.location.id].depth = node.depth + 1
                    nodes[ch.location.id].parent = node.location.id
                    if ch.location.id in visited_nodes: #remove the node from visited_nodes and push it again in frontier
                        visited_nodes.remove(ch.location.id)
                        heapq.heappush(frontier,(nodes[ch.location.id].heur,nodes[ch.location.id]))
                        #print "pushed {0} ({1},{2})".format(ch.location.id,ch.location.x,ch.location.y)

        i += 1

    return (False,0,0,0)
"""
Find and print the path from the node v1 to the node v2.
"""
def print_path(v1,v2):
    path = []
    i = v2
    while i != None:
        path.append(nodes[i])
        i = nodes[i].parent

    print "solution path:"

    for v in reversed(path):
        print " vertex {0} ({1},{2})".format(v.location.id,v.location.x,v.location.y)

#sys.stdout = open("output3.txt","w")

test = Parser(str(sys.argv[1]))
nodes = test.parseFile()

i_state = findNode(int(sys.argv[2]),int(sys.argv[3]))
g_state = findNode(int(sys.argv[4]),int(sys.argv[5]))

"""
Perform the search if both nodes exists in the graph.
"""
if i_state is not None and g_state is not None:
    print "start=({0},{1}), goal=({2},{3}), vertices: {4} and {5}".format(i_state.location.x,i_state.location.y,g_state.location.x,g_state.location.y,i_state.location.id,g_state.location.id)
    goal_found = False
    search_algo = ''
    function = str(sys.argv[6]).lower()
    if function == 'b':
        search_algo = 'BFS'
        (goal_found,it,fr_size,visited) = BFS(i_state,g_state)
    elif function == 'd':
        search_algo = 'DFS'
        (goal_found,it,fr_size,visited) = DFS(i_state,g_state)
    elif function == 'g':
        search_algo = 'GBFS'
        (goal_found,it,fr_size,visited) = GBFS(i_state,g_state)
    else:
        print "ERROR: There is no function that matchs the given character {0}".format(function)

    print "================="
    if goal_found == False:
        print "There is no path from the vertex {0} to the vertex {1}".format(i_state.location.id,g_state.location.id)
    else:
        print_path(i_state.location.id,g_state.location.id)
        print "search algorithm = {0}".format(search_algo)
        print "total iterations = {0}".format(it)
        print "max frontier size= {0}".format(fr_size)
        print "vertices visited = {0}/{1}".format(visited,len(nodes))
        print "path length = {0}".format(g_state.depth)
else:
    print "The vertices with coordinates ({0},{1}) and/or ({2},{3}) does not exists in this graph.".format(int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))