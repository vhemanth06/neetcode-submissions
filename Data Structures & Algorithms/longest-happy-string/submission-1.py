class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap=[]
        if a!=0:
            heapq.heappush(heap,[-a,'a'])
        if b!=0:
            heapq.heappush(heap,[-b,'b'])
        if c!=0:
            heapq.heappush(heap,[-c,'c'])
        res=[]
        prev='d'
        # print(heap)
        while heap:
            
            x,y=heapq.heappop(heap)
            if prev==y:
                if heap:
                    z,t=heapq.heappop(heap)
                    heapq.heappush(heap,[x,y])
                    # x,y=z,t
                    res.append(t)
                    prev=t
                    if z+1!=0:
                        heapq.heappush(heap,[z+1,t])
                else:
                    return "".join(res)
            else:
                res.append(y)
                if x<-1:
                    res.append(y)
                prev=y
                if x+2<0:
                    heapq.heappush(heap,[x+2,y])
            # print(res)
        return "".join(res)
