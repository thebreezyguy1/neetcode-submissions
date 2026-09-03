# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head

        while list1 or list2:
            if (list1 and list2 and list1.val <= list2.val) or (list1 and not list2):
                temp.next = ListNode(list1.val)
                print(temp.val)
                temp = temp.next
                list1 = list1.next
            elif list2:
                temp.next = ListNode(list2.val)
                temp = temp.next
                list2 = list2.next
        
        return head.next
