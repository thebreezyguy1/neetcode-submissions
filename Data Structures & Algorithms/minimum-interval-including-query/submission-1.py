class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        
        n = len(queries)
        h = []
        res = [-1] * n
        i = 0

        for q, idx in sorted((q, i) for i, q in enumerate(queries)):
            while i < len(intervals) and intervals[i][0] <= q:
                size = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(h, (size, intervals[i][1]))
                i += 1
            
            while h and h[0][1] < q:
                heapq.heappop(h)
            
            if h:
                res[idx] = h[0][0]
        
        return res