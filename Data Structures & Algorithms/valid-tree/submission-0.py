class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        adj=[[] for _ in range(n)]
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)
        q=deque()
        visited=set()
        q.append([0,-1])
        visited.add(0)
        while q:
            x,px=q.popleft()
            for y in adj[x]:
                if y==px:
                    continue
                elif y not in visited:
                    visited.add(y)
                    q.append([y,x])
                else:
                    return False

        return len(visited)==n