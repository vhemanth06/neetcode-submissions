from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=set()
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        res=0
        def bfs(i,j):
            # if (i,j) in visited :
            #     return False
            visited.add((i,j))
            queue=deque([(i,j)])
            while queue:
                x,y=queue.popleft()
                # print(f"Visiting {x},{y}")
                # visited.add((x,y))
                for dx,dy in d:
                    nx=x+dx
                    ny=y+dy
                    if nx<0 or ny<0 or nx>=m or ny>=n or grid[nx][ny]=='0':
                        continue
                    else:
                        if (nx,ny) not in visited:

                            queue.append((nx,ny))
                            visited.add((nx,ny))
            return True
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visited:
                    bfs(i,j)
                    res+=1
        return res


