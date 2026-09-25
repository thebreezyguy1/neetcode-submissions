class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Brute-force approach
        # n = len(s)

        # def dfs(start):
        #     if start == n:
        #         return True
            
        #     res = False
        #     for word in wordDict:
        #         if s[start:].startswith(word):
        #             res = res or dfs(start + len(word))
            
        #     return res
        
        # return dfs(0)

        # TopDown DP
        # n = len(s)
        # memo = {}

        # def dfs(start):
        #     if start == n:
        #         return True
        #     if start in memo:
        #         return memo[start]
            
        #     res = False
        #     for word in wordDict:
        #         if s[start:].startswith(word):
        #             res = res or dfs(start + len(word))
            
        #     memo[start] = res
        #     return res
        
        # return dfs(0)

        # Bottom-up approach
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n-1, -1, -1):
            for word in wordDict:
                if s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    if dp[i]:
                        break
        
        return dp[0]