class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        alist=defaultdict(list)
        for x,y in edges:
            alist[x].append(y)
            alist[y].append(x)
        visited=set()
        def bfs(start):
            visited.add(start)
            q=deque()
            q.append(start)
            while q:
                x=q.popleft()
                for nx in alist[x]:
                    if nx not in visited:
                        visited.add(nx)
                        q.append(nx)
        res=0
        for i in range(n):
            if i not in visited:
                bfs(i)
                res+=1
        return res


