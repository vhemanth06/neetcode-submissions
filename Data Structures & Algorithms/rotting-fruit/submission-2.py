from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        m,n=len(grid),len(grid[0])
        one=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    one+=1
        d=[[1,0],[-1,0],[0,1],[0,-1]]
        # visited=set()
        if not q:
            if one:
                return -1
            else:
                return 0
        l=-1
        while q:
            dia=len(q)
            print(q)
            l+=1
            for _ in range(dia):
                x,y=q.popleft()
                # grid[x][y]=2
                for dx,dy in d:
                    nx,ny=x+dx,y+dy
                    if nx>=0 and nx<m and ny>=0 and ny<n and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        q.append((nx,ny))
            # l+=1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return l