class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # n = len(s)
        # char_found = set(s[0])
        # count = Counter(s)
        # left, right = 0, 0
        # res = []

        # while right < n:
        #     if s[right] not in char_found:
        #         char_found.add(s[right])
        #     count[s[right]] -= 1
        #     if count[s[right]] == 0:
        #         char_found.remove(s[right])
        #     if len(char_found) == 0:
        #         res.append(right - left + 1)
        #         left = right + 1
        #     right += 1
        
        # return res

        last_indices = {}

        for char in set(s):
            last_indices[char] = s.rindex(char)
        size = 0
        left = 0
        res = []

        for i in range(len(s)):
            size = max(size, last_indices[s[i]] - left + 1)
    
            if i == left + size - 1:
                res.append(size)
                left = i + 1
                size = 0
        
        return res