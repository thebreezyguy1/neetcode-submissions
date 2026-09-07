# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        blocks = []

        temp = head
        count = 0
        block = []
        while temp:
            block.append(temp)
            count += 1
            if count % k == 0:
                blocks.append(block)
                block = []
            temp = temp.next
        blocks.append(block)
        
        blocks = [block[::-1] if len(block) == k else block for block in blocks]

        # blocks = []
        # for block in nodes:
        #     if len(block) == k:
        #         blocks.append(block[::-1])
        #     else:
        #         blocks.append(block)
        # print([[node.val for node in block] for block in blocks])

        res = temp = ListNode()

        for block in blocks:
            for node in block:
                temp.next = node
                temp = temp.next
        temp.next = None
        
        return res.next


        

            
            