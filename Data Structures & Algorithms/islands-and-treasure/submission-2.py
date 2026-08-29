from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m,n=len(grid),len(grid[0])
        d=[[0,1],[0,-1],[1,0],[-1,0]]
        queue=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 :
                    queue.append((i,j))
    
        visited=set()
        l=0
        while queue:
            nl=len(queue)
            
            for i in range(nl):
                x,y=queue.popleft()
                grid[x][y]=l
                # print(f"level={l} x,y={x},{y}")
                for dx,dy in d:
                    nx,ny=x+dx,y+dy
                    if nx>=m or ny>=n or nx<0 or ny<0 or grid[nx][ny]==-1 or grid[nx][ny]==0 or (nx,ny) in visited:
                        continue
                    else:
                        # grid[nx][ny]=min(grid[nx][ny],l)
                        visited.add((nx,ny))
                        queue.append((nx,ny))
            l+=1
    
    






