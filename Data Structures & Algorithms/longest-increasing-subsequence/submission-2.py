class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {}

        def dfs(start, path):
            if start == n:
                return 0
            if start in memo:
                return memo[start]
            
            res = 0
            for i in range(start, n):
                if not path or nums[i] > path[-1]:
                    res = max(res, 1 + dfs(i + 1, path + [nums[i]]))
            memo[start] = res
            return res

        return dfs(0, [])