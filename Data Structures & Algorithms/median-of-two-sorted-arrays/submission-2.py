class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # Brute-force approach
        # nums = nums1 + nums2
        # nums.sort()
        # n = len(nums)
        # half = n // 2
        # return nums[half] if n % 2 == 1 else ((nums[half] + nums[half - 1]) / 2)

        # Two pointers
        n, m = len(nums1), len(nums2)
        count = 0
        p, q = 0, 0
        median1, median2 = 0, 0

        while count < ((n + m) // 2 + 1):
            median2 = median1
            if p < n and q < m:
                if nums1[p] < nums2[q]:
                    median1 = nums1[p]
                    p += 1
                else:
                    median1 = nums2[q]
                    q += 1
            elif p < n:
                median1 = nums1[p]
                p += 1
            else:
                median1 = nums2[q]
                q += 1
            count += 1
        
        if (n + m) % 2 == 1:
            return median1
        
        return (median1 + median2) / 2

        