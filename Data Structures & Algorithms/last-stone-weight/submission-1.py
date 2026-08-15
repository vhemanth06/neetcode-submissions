import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        x=[-n for n in stones]
        heapq.heapify(x)
        while len(x)>1:
            x1=-heapq.heappop(x)
            x2=-heapq.heappop(x)
            if x1==x2:
                continue
            else:
                heapq.heappush(x,-(x1-x2))
        if not x:
            return 0
        else:
            return -x[0]
        