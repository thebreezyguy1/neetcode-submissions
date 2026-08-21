class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def dfs(i, buying, cache):
            if i >= n:
                return 0
            
            if (i, buying) in cache:
                return cache[(i, buying)]
            
            if buying:
                total = dfs(i + 1, False, cache) - prices[i]
            else:
                total = dfs(i + 2, True, cache) + prices[i]
            
            cache[(i, buying)] = max(total, dfs(i + 1, buying, cache))


            return cache[(i, buying)]
        
        return dfs(0, True, {})