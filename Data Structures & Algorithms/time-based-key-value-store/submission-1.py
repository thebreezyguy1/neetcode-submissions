from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.store[key]
        if not timestamps:
            return ""
        index = bisect_right(timestamps, timestamp, key=lambda x:x[0])
        if index == 0:
            return ""
        return timestamps[index - 1][1]
        
