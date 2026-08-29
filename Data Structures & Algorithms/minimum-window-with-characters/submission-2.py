class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # Brute-force approach
        # n = len(s)

        # res = ""
        # resLen = float('inf')

        # for i in range(n):
        #     for j in range(i, n):
        #         sub = s[i:j+1]
        #         if set(t) <= set(sub) and resLen > len(sub):
        #             res = sub
        #             resLen = len(res)
        
        # return res

        # Sliding window
        n = len(s)
        window_counter = [0] * 58
        target_counter = [0] * 58

        for c in t:
            target_counter[ord(c) - 65] += 1
        
        have = 0
        need = len(target_counter) - target_counter.count(0)

        print(target_counter)
        
        res = ""
        resLen = float("inf")

        left = 0

        for right in range(n):
            index = ord(s[right]) - 65
            window_counter[index] += 1
            if window_counter[index] == target_counter[index]:
                have += 1
            while have >= need:
                length = right - left + 1
                if resLen > length:
                    res = s[left: right + 1]
                    resLen = length
                index = ord(s[left]) - 65
                window_counter[index] -= 1
                if s[left] in t and window_counter[index] < target_counter[index]:
                    have -= 1
                left += 1
        
        return res

