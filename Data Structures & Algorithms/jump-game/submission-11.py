class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = {}
        def dfs(i):
            if i == n - 1:
                return True
            if i in memo:
                return memo[i]
             
            res = False
            for j in range(1, nums[i] + 1):
                res = res or dfs(i + j)
            
            memo[i] = res
            return res
        
        return dfs(0)
            
