from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        queue = deque()
        h = []
        frequencies = Counter(tasks)
        time = 0

        for task, freq in frequencies.items():
            heapq.heappush(h, (-freq, task))

        while h or queue:
            time += 1
            
            if not h:
                time = queue[0][2]
            else:
                freq, task = heapq.heappop(h)
                freq *= -1
                if freq > 1:
                    queue.append((task, freq - 1, time + n))
            if queue and queue[0][2] == time:
                task, freq, task_time = queue.popleft()
                heapq.heappush(h, (-(freq), task))
        
        return time
