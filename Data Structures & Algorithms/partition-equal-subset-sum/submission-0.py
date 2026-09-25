class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if total % 2 != 0:
            return False
        
        def dfs(count, path):
            if count == total // 2:
                return True
            
            res = False
            for i in range(n):
                if i not in path and count + nums[i] <= total // 2:
                   res = res or dfs(count + nums[i], path + [i])
            
            return res
        
        return dfs(0, [])

