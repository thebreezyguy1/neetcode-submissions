class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(total):
            if total == amount:
                return 0
            if total in memo:
                return memo[total]
            
            res = float("inf")
            for coin in coins:
                if total + coin <= amount:
                    res = min(res, 1 + dfs(total + coin))
            
            memo[total] = res
            return res

        min_coins = dfs(0)
        return -1 if min_coins == float("inf") else min_coins
