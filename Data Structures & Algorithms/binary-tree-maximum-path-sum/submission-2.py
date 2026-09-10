# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            leftDown = dfs(root.left)
            rightDown = dfs(root.right)

            leftMax = max(0, leftDown)
            rightMax = max(0, rightDown)

            res = max(res, root.val + leftMax + rightMax)

            return max(0, root.val + max(leftMax, rightMax))
        
        dfs(root)
        return res