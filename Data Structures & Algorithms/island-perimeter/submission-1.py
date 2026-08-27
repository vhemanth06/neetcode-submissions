from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        visit=set()
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(i,j):
            queue=deque([(i,j)])
            visit.add((i,j))
            perimeter=0
            while queue:
                x,y=queue.popleft()
                for dx,dy in d:
                    nx,ny=x+dx,y+dy
                    if nx>=m or ny>=n or nx<0 or ny<0 or grid[nx][ny]==0:
                        perimeter+=1
                    elif (nx,ny) not in visit:
                        visit.add((nx,ny))
                        queue.append((nx,ny))
            return perimeter
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return bfs(i,j)

