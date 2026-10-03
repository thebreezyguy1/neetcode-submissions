class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # memo = {}

        # def dfs(i):
        #     if i == n - 1:
        #         return True
        #     if i in memo:
        #         return memo[i]
             
        #     res = False
        #     for j in range(1, nums[i] + 1):
        #         res = res or dfs(i + j)
            
        #     memo[i] = res
        #     return res
        
        # return dfs(0)

        # n = len(nums)
        # dp = [False] * n
        # dp[n - 1] = True

        # for i in range(n-2, -1, -1):
        #     end = min(n, i + nums[i] + 1)
        #     for j in range(i+1, end):
        #         dp[i] = dp[i] or dp[j]
        
        # return dp[0]

        n = len(nums)
        goal = n - 1

        for i in range(n-2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i+1, end):
                print(j, goal)
                if j == goal:
                    goal = i
                    break
        
        return True if goal == 0 else False
            
