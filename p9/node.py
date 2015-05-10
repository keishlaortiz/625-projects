"""
Keishla D. Ortiz Lopez
CSCE 625 - Artificial Intelligence

P9: Goal regression for planning in the Blocksworld

Node class
"""

class Node(object):
    def __init__(self,goals=[],plan=[]):
        self._goals = goals
        self._plan = plan

    @property
    def goals(self):
        return self._goals

    @property
    def plan(self):
        return self._plan

    @property
    def priority(self):
        return len(self.plan)

    #used to sort the queue
    def __len__(self):
        return len(self.plan)