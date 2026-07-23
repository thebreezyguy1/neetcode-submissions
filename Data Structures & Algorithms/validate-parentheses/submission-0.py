class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = []
        dic = {"(":")", "{":"}", "[":"]"}
        for char in s:
            if char in dic.keys():
                stack.append(char)
            else:
                if len(stack) == 0 or dic[stack.pop()] != char:
                    return False
        
        return True if len(stack) == 0 else False