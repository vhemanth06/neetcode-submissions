class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        if n==2:
            return [0,1]
        adj=[[] for _ in range(n)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        cnt=defaultdict(int)
        source=deque()
        for i in range(len(adj)):
            cnt[i]=len(adj[i])
            if len(adj[i])==1:
                source.append(i)
        while source:
            if n<=2:
                return list(source)
            for i in range(len(source)):
                x=source.popleft()
                n-=1
                for y in adj[x]:
                    cnt[y]-=1
                    if cnt[y]==1:
                        source.append(y)
