class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cap=[]
        pro=[]
        for i,c in enumerate(capital):
            if c<=w:
                heapq.heappush(pro,-profits[i])
            else:
                heapq.heappush(cap,[c,-profits[i]])
        
        # print(cap)
        # print(pro)
        while k and pro:
            # print(f"{w}  {pro}  {cap}  {k}")
            x=-heapq.heappop(pro)
            w+=x
            while cap and cap[0][0]<=w:
                c,p=heapq.heappop(cap)
                heapq.heappush(pro,p)
            k-=1
        return w

        