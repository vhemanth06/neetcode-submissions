class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n=len(grid),len(grid[0])
        visited=set()
        res=0
        def dfs(i,j):
            if i>=m or j>=n or i<0 or j<0 or grid[i][j]=='0' or (i,j) in visited:
                return 
            # print(f"Visited {i},{j}")
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1' and (i,j) not in visited:
                    dfs(i,j)
                    res+=1
        return res
            