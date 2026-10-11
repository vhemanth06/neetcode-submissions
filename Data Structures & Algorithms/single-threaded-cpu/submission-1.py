class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap=[]
        idle=[]
        res=[]
        n=len(tasks)
        time=0
        for i in range(n):
            heapq.heappush(heap,[tasks[i][0],tasks[i][1],i])
        prev=-1
        while heap:
            # print(f"{time} ")
            # start,dur,x=heap[0]
            while heap and heap[0][0]<=time:
                
                start,dur,x=heapq.heappop(heap)
                heapq.heappush(idle,[dur,start,x])
            if idle:
                dur,start,x=heapq.heappop(idle)
                time+=dur
                res.append(x)
            else:
                time=heap[0][0]
        while idle:
            start,dur,x=heapq.heappop(idle)
            res.append(x)
            
                
            # res.append(x)
        return res