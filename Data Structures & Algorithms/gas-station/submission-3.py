class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        end, start = 0, len(gas) - 1
        tank = 0

        tank = gas[start] - cost[start]

        while end < start:
            if tank < 0:
                start -= 1
                tank += gas[start] - cost[start]
            else:
                tank += gas[end] - cost[end]
                end += 1
        
        return -1 if tank < 0 else start


        # n = len(gas)
        # count = 0
        # i = 0

        # for i in range(n):
        #     count = 0
        #     tank = gas[i] - cost[i]
        #     while count < n and tank >= 0:
        #         count += 1
        #         j = (i + count) % n
        #         tank += gas[j] - cost[j]
            
        #     if count == n:
        #         return i
        
        # return -1
             


