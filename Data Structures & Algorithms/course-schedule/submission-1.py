class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(n)]
        for x,y in prerequisites:
            adj[x].append(y)
        # print(grid)
        visited=set()
        def dfs(i):
            if i in visited:
                return False
            if adj[i]==[]:
                return True
            visited.add(i)
            for y in adj[i]:
                if not dfs(y):
                    return False
            visited.remove(i)
            adj[i]=[]
            return True
        for i in range(n):
            if not dfs(i):
                return False
        return True
        