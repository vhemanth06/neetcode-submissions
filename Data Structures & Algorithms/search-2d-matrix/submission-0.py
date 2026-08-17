class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        def bn(i,j):
            if i >= m or j<0:return False
            if target<matrix[i][j]:
                return bn(i,j-1)
            elif target>matrix[i][j]:
                return bn(i+1,j)
            else:
                return True
        return bn(0,n-1)
