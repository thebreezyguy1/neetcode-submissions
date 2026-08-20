"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        for i in range(1, len(intervals)):
            x1, y1 = intervals[i - 1].start, intervals[i - 1].end
            x2, y2 = intervals[i].start, intervals[i].end
            if y2 < x1 or x2 < y1:
                return False
        
        return True