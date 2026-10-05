class Solution:
    def jump(self, nums: List[int]) -> int:
        # n = len(nums)
        # memo = {}

        # def dfs(i):
        #     if i == n - 1:
        #         return 0
        #     if i in memo:
        #         return memo[i]
            
        #     res = float("inf")
        #     end = min(n, i + nums[i] + 1)
        #     for j in range(i + 1, end):
        #         res = min(res, dfs(j) + 1)
            
        #     memo[i] = res
        #     return res
        
        # return dfs(0)
        
        n = len(nums)
        dp = [float("inf")] * n
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i+1, end):
                dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[0]