class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        p=matrix
        m,n=len(matrix),len(matrix[0])
        for i in range(1,m):
            p[i][0]+=p[i-1][0]
        for i in range(1,n):
            p[0][i]+=p[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                p[i][j]+=(p[i-1][j]+p[i][j-1]-p[i-1][j-1])
        self.prefix=p
        # print(p)
    


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x1=self.prefix[row2][col2]
        x2=0
        y1=0
        y2=0
        if row1>0 and col1>0:
            x2=self.prefix[row1-1][col1-1]
        if row1>0:
            y1=self.prefix[row1-1][col2]
        if col1>0:
            y2=self.prefix[row2][col1-1]
        return x1+x2-y1-y2


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)