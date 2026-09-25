class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Brute-force approach
        # n = len(nums)
        # res = -float("inf")

        # for i in range(n):
        #     for j in range(i, n):
        #         total = sum(nums[i:j+1])
        #         res = max(res, total)
        
        # return res

        # Sliding Window
        n = len(nums)
        total = 0
        currMax = -float("inf")

        for i in range(n):
            temp = total + nums[i]
            total = max(total + nums[i], nums[i])
            currMax = max(currMax, temp, nums[i])
        
        return currMax
