class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Brute-force approach
        # n = len(s)
        # longest = ""

        # for i in range(n):
        #     for j in range(i, n):
        #         sub = s[i: j + 1]
        #         if sub == sub[::-1] and len(sub) > len(longest):
        #             longest = sub
        
        # return longest

        n = len(s)
        dp = [[False] * (n) for i in range(n)]
        resIdx, resLen = 0, 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i <= 2) or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if (j - i + 1) > resLen:
                        resIdx = i
                        resLen = j - i + 1
                        print(resLen)
        
        return s[resIdx: resIdx + resLen]
