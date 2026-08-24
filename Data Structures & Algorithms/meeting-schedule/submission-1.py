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
        prev=0
        for i in range(len(intervals)):
                if i!=0 and prev>intervals[i].start:
                    return False
                prev=intervals[i].end
        return True