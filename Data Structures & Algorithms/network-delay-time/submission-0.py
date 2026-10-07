class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for x,y,z in times:
            adj[x].append([y,z])
        dist=[float('inf')]*(n+1)
        heap=[(0,k)]
        dist[k]=0
        while heap:
            x,y=heapq.heappop(heap)
            for nei,wei in adj[y]:
                if wei+x<dist[nei]:
                    dist[nei]=wei+x
                    heapq.heappush(heap,(wei+x,nei))
        res=max(dist[1:])
        return res if res!=float('inf') else -1