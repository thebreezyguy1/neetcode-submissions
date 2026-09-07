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
        
        oldToNew = {}

        copy = temp1 = Node(0)
        temp2 = head

        while temp2:
            node = Node(temp2.val)
            oldToNew[temp2] = node
            temp1.next = node
            temp1 = temp1.next
            temp2 = temp2.next
        
        temp1 = copy.next
        temp2 = head

        while temp2:
            if temp2.random:
                temp1.random = oldToNew[temp2.random]
            temp1 = temp1.next
            temp2 = temp2.next
        
        return copy.next
