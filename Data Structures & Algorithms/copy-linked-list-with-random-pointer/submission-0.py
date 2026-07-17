"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        deep_copies = { None : None }
        curr = head

        while curr:
            copy = Node(curr.val)
            deep_copies[curr] = copy
            curr = curr.next
        
        curr = head

        while curr:
            copy = deep_copies[curr]
            copy.next = deep_copies[curr.next]
            copy.random = deep_copies[curr.random]
            curr = curr.next
        
        return deep_copies[head]