class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # TODO: DP Top Down Solution
        
        open_stack = []
        star_stack = []

        for i, c in enumerate(s):
            if c == "(":
                open_stack.append(i)
            if c == "*":
                star_stack.append(i)
            if c == ")":
                if open_stack:
                    open_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        
        while star_stack:
            if not open_stack:
                return True
            star_idx = star_stack.pop()
            open_idx = open_stack.pop()
            if open_idx > star_idx:
                return False

        return len(open_stack) == 0
