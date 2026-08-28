from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=set()
        d=[(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(i,j):
            visited.add((i,j))
            queue=deque([(i,j)])
            res=0
            while queue:
                res+=1
                x,y=queue.popleft()
                # print(f"visiting {x},{y}")
                for dx,dy in d:
                    nx, ny=x+dx,y+dy
                    if nx<m and ny<n and nx>=0 and ny>=0 and grid[nx][ny]==1 and (nx,ny) not in visited:
                        queue.append((nx,ny))
                        visited.add((nx,ny))
                        
            return res
        res=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    res=max(res,bfs(i,j))
        return res
            
                    
