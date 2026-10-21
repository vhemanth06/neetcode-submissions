class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        res=[0]*n
        idle=[i for i in range(n)]
        ending=[]
        heapq.heapify(idle)

        for start,end in meetings:
            while ending and start>=ending[0][0]:
                x,y=heapq.heappop(ending)
                heapq.heappush(idle,y)
            if idle:
                y=heapq.heappop(idle)
                heapq.heappush(ending,[end,y])
     
            else:
                x,y=heapq.heappop(ending)
                heapq.heappush(ending,[end+x-start,y])
            res[y]+=1
    

        

        return res.index(max(res))
