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
        
        # 2D DP
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # res = 0

        # for i in range(n-1, -1, -1):
        #     for j in range(n-1, -1, -1):
        #         if j >= i and s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
        #             dp[i][j] = True
        #             res += 1
        
        # return res

        n = len(s)
        res = 0

        # odd-length palindromes
        for i in range(n):
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        # even-length palindromes
        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res