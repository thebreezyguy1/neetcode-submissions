# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Brute-force approach
        # nodes = []

        # temp = head

        # while temp:
        #     nodes.append(temp)
        #     temp = temp.next
        
        # i, j = 0, len(nodes) - 1

        # while i < j:
        #     nodes[i].next = nodes[j]
        #     i += 1
        #     if i == j:
        #         break
        #     nodes[j].next = nodes[i]
        #     j -= 1
        
        # nodes[j].next = None

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        prev = slow.next = None

        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp
        
        l1, l2 = head, prev

        while l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l2.next = temp1
            l1, l2 = temp1, temp2
            