class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # Brute-force approach
        # n = len(nums)
        # res = -float("inf")

        # for i in range(n):
        #     product = 0
        #     for j in range(i, n):
        #         if j - i == 0:
        #             product = nums[i]
        #         else:
        #             product *= nums[j]
        #         res = max(res, product)

        # return res

        currMax, currMin = 1, 1
        res = nums[0]

        for i in range(len(nums)):
            temp = nums[i] * currMax
            currMax = max(temp, nums[i] * currMin, nums[i])
            currMin = min(temp, nums[i] * currMin, nums[i])
            res = max(res, currMax)
        
        return res