class Solution:
    def numDecodings(self, s: str) -> int:
        # n = len(s)

        # def dfs(start, memo):
        #     if start == n:
        #         return 1
        #     if start in memo:
        #         return memo[start]

        #     ans = 0
        #     if int(s[start]) == 0:
        #         return ans
            
        #     ans += dfs(start + 1, memo)
            
        #     if 10 <= int(s[start: start + 2]) <= 26:
        #         ans += dfs(start + 2, memo)
            
        #     memo[start] = ans
        #     return ans
        
        # return dfs(0, {})
        n = len(s)

        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            if int(s[i]) == 0:
                continue
            dp[i] = dp[i + 1]
            if 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]
        
        return dp[0]
