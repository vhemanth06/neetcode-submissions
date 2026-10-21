class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        d=[[1,0],[-1,0],[0,1],[0,-1]]
        # self.maxum=-1
        cache=defaultdict(int)
        def dp(x,y):
            # if x>=m or x<0 or y>=n or y<0 :
            #     return 0
            if (x,y) in cache:
                return cache[(x,y)]
            res=1
            for dx,dy in d:
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and matrix[nx][ny]>matrix[x][y]:
                    res=max(res,1+dp(nx,ny))
            # self.maxum=max(self.maxum,res)
            cache[(x,y)]=res
            return res
        for i in range(m):
            for j in range(n):
                dp(i,j)
        return max(cache.values())

        

            

        