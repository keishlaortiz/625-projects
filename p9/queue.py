"""
Keishla D. Ortiz Lopez
CSCE 625 - Artificial Intelligence

P9: Goal regression for planning in the Blocksworld

Queue class for the goal_regression function
"""

from node import Node
import heapq

class Queue(object):

    def __init__(self):
        self._queue = []

    """
    item should have a priority attribute
    """
    def push(self,item):
        heapq.heappush(self._queue,(item.priority,item))

    def pop(self):
        if len(self._queue) != 0:
            return heapq.heappop(self._queue)[1]

    def __len__(self):
        return len(self._queue)

#test class
def main():
    queue = Queue()
    item = Node([],[1,2])
    queue.push(item)
    item = Node([],[0])
    queue.push(item)
    item = Node([],[2,39,92,29])
    queue.push(item)
    item = Node([],[])
    queue.push(item)
    item = Node([],[1])
    queue.push(item)
    while len(queue) != 0:
        print queue.pop().plan

if __name__ == '__main__':
    main()
