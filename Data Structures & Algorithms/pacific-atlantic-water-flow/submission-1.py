class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        p=[]
        for i in range(m):
            p.append((i,0))
        for j in range(n):
            p.append((0,j))
        a=[]
        for i in range(m):
            a.append((i,n-1))
        for j in range(n):
            a.append((m-1,j))
        d=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(sources):
            visited=set(sources)
            q=deque(sources)
            while q:
                x,y=q.popleft()
                for dx,dy in d:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n and heights[nx][ny]>=heights[x][y] and (nx,ny) not in visited:
                        q.append((nx,ny))
                        visited.add((nx,ny))
            return visited
        x,y=bfs(p),bfs(a)
        res=[]
        for i in range(m):
            for j in range(n):
                if (i,j) in x and (i,j) in y:
                    res.append([i,j])
        return res
