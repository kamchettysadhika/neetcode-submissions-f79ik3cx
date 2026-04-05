"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# create a hashmao and create two passes one for nodes and 
# the other for pointers (Random/next)
# and add all the nodes to that 
# 
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None:None}
        # old -> copy
        cur = head 
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next 
        # second pass to copy links 
        cur = head 
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next 
        return oldToCopy[head]



        # copy nodes 
        # linkes 
        # Two pass hashmap 
