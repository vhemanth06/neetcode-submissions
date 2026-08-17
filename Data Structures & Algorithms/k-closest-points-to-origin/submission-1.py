import heapq
import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kclo=[]
        for p in points:
            x,y=p
            d=x**2+y**2
            heapq.heappush(kclo,(-d,[x,y]))
            if len(kclo)>k:
                heapq.heappop(kclo)
        return [p[1] for p in kclo ]