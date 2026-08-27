class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i>=m or j>=n or i<0 or j<0 or grid[i][j]==0:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            return dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)
         
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i,j)
