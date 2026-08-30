class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(n)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        def bfs(i):
            visited=set()
            visited.add(i)
            q=deque()
            q.append(i)
            h=0
            while q:
                l=len(q)
                for _ in range(l):
                    x=q.popleft()
                    for num in adj[x]:
                        if num not in visited:
                            visited.add(num)
                            q.append(num)
                h+=1
            return h
        res=[]
        hmin=n
        for i in range(n):
            x=bfs(i)
            if x<hmin:
                res=[i]
                hmin=x
            elif x==hmin:
                res.append(i)
        return res
        
