
# pqueue.py -- an implementation of priority queues using Python's heapq.

# A "decrease key" operation is implemented by marking updated entries but
# otherwise leaving them in the heap until they are found (and removed and
# ignored) by a pop operation.  The updated entry is inserted using heappush
# (with the updated priority) to obtain O(log n) update performance.

import heapq

invalid = '#invalid#'

# priority queue internal representation

# q[0] (size) keeps track of the total number of valid entries in the queue.

# q[1] is a dictionary of handles on an entry ([priority, item]), which are
#      otherwise unavailable, enabling an item to be invalidated by
#      destructively modifying the list.

# q[2] (heap) is a list maintained by heapq operations as a heap.

#Code taken from http://www4.ncsu.edu/~jwb/courses/537/f12/hw/pqueue.py

def queue(init={}):
    q = [0, dict(), []]         # [size, dict, heap]
    for key, value in init.iteritems():
        enqueue(q, value, key)
    return q

def enqueue(q, priority, item):
    q[0] += 1
    entry = [priority, item]
    q[1][repr(item.block)] = entry
    heapq.heappush(q[2], entry)

def size(q):
    return q[0]

def dequeue(q):
    priority, item = _pop(q)
    while item == invalid:
        priority, item = _pop(q)
    q[0] -= 1
    return priority, item

def _pop(q):
    priority, item = heapq.heappop(q[2])
    if item != invalid:
        del q[1][repr(item.block)]
    return priority, item

def update(q, priority, item):
    entry = q[1][repr(item.block)]
    entry[1] = invalid
    new_entry = [priority, item]
    q[1][repr(item.block)] = new_entry
    heapq.heappush(q[2], new_entry)
