"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        q=[]
        heapq.heapify(q)
        for i in intervals:
            if q and i.start>=q[0]:
                heapq.heappop(q)
            heapq.heappush(q,i.end)
            # print(q[0])
        return len(q)