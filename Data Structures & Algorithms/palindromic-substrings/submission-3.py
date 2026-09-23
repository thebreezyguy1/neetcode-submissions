class Solution:
    def countSubstrings(self, s: str) -> int:
        # Brute-force approach
        # n = len(s)
        # count = 0

        # for i in range(n):
        #     for j in range(i, n):
        #         if s[i:j+1] == s[i:j+1][::-1]:
        #             count += 1
        
        # return count

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if j >= i and s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        
        return res