class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        #Brute-force approach
        # n = len(heights)
        # max_area = 0

        # for i in range(n):
        #     for j in range(i, n):
        #         section = heights[i: j + 1]
        #         min_height = min(section)
        #         width = len(section)
        #         area = min_height * width
        #         max_area = max(max_area, area)
        
        # return max_area

        n = len(heights)
        stack = []

        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        
        stack = []
        rightMost = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for i in range(n):
            leftMost[i] += 1
            rightMost[i] -= 1
            max_area = max(max_area, heights[i] * (rightMost[i] - leftMost[i] + 1))

        return max_area
        

