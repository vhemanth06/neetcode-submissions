class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res=[]
        m,n=len(heights),len(heights[0])
        d=[[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(i,j):
            visited=set()
            visited.add((i,j))
            q=deque()
            q.append((i,j))
            p,a=False,False
            while q:
                x,y=q.popleft()
                for dx,dy in d:
                    nx,ny=x+dx,y+dy
                    if nx<0 or ny<0 :
                        p=True
                        continue
                    if nx>=m or ny>=n:
                        a=True
                        continue
                    if a and p:
                        return True
                    if heights[nx][ny]<=heights[x][y] and (nx,ny) not in visited:
                        visited.add((nx,ny))
                        q.append((nx,ny))
            return a and p
        
        for i in range(m):
            for j in range(n):
                if bfs(i,j):
                    res.append([i,j])
        return res
                    
