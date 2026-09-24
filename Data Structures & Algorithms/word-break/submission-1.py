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
        n = len(s)
        memo = {}

        def dfs(start):
            if start == n:
                return True
            if start in memo:
                return memo[start]
            
            res = False
            for word in wordDict:
                if s[start:].startswith(word):
                    res = res or dfs(start + len(word))
            
            memo[start] = res
            return res
        
        return dfs(0)