class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # n = len(nums)
        # memo = {}

        # def dfs(start, prev):
        #     if start == n:
        #         return 0
        #     if start in memo:
        #         return memo[start]
            
        #     res = 0
        #     for i in range(start, n):
        #         if prev == -1 or nums[i] > nums[prev]:
        #             res = max(res, 1 + dfs(i + 1, i))
        #     memo[start] = res
        #     return res

        # return dfs(0, -1)

        n = len(nums)
        dp = [1] * n

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)