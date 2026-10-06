class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=defaultdict(list)
        for x,y,z in flights:
            adj[x].append((y,z))
        dist=[[float('inf')]*(k+2) for _ in range(n)]
        dist[src][0]=0
        heap=[(0,0,src)]
        while heap:
            x,z,y=heapq.heappop(heap)
            for nei,wei in adj[y]:
                newdist=wei+x
                if z<k+1 and  newdist<dist[nei][z+1]  :
                    dist[nei][z+1]=newdist
                    heapq.heappush(heap,(newdist,z+1,nei))
        res=min(dist[dst])
        return res if res!=float('inf') else -1
