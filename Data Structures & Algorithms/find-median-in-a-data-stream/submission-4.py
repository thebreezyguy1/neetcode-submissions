from heapq import heappush, heappop 
class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.maxHeap and not self.minHeap:
            heappush(self.maxHeap, -num)
        elif self.maxHeap and -self.maxHeap[0] > num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        if abs(len(self.maxHeap) - len(self.minHeap)) >= 2:
            if len(self.minHeap) > len(self.maxHeap):
                heappush(self.maxHeap, -heappop(self.minHeap))
            else:
                heappush(self.minHeap, -heappop(self.maxHeap))

    def findMedian(self) -> float:
        if not self.minHeap or len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        