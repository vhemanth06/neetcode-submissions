class Solution:
    def reorganizeString(self, s: str) -> str:
        freq=[0]*26
        for c in s:
            freq[ord(c)-ord('a')]-=1
        heap=[]
        for i in range(26):
            if freq[i]!=0:
                heapq.heappush(heap,[freq[i],chr(ord('a')+i)])
        res=[]
        prev='#'
        while heap:
            x,y=heapq.heappop(heap)
            if prev==y:
                if heap:
                    z,t=heapq.heappop(heap)
                    heapq.heappush(heap,[x,y])
                    x,y=z,t
                else:
                    return ""
            res.append(y)
            prev=y
            if x+1!=0:
                heapq.heappush(heap,[x+1,y])
        return "".join(res)




        
        