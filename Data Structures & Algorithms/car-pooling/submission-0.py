class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cap=defaultdict(int)
        for num,start,end in trips:
            cap[start]+=num
            cap[end]-=num
        print(cap)
        heap=[]
        for x,y in cap.items():
            if y>capacity:
                return False
            else:
                heapq.heappush(heap,[x,y])
        cur=0
        while heap:
            x,y=heapq.heappop(heap)
            cur+=y
            if cur>capacity:
                return False
                
        return True
