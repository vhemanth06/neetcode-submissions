class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix),len(matrix[0])
        i1,i2,j1,j2=0,len(matrix)-1,0,len(matrix[0])-1
        
        res=[]
        while i1<=i2 and j1<=j2:
            for j in range(j1,j2+1):
                res.append(matrix[i1][j])
            i1+=1
            for j in range(i1,i2+1):
                res.append(matrix[j][j2])
            j2-=1
            if i1<=i2:
                for j in range(j2,j1-1,-1):
                    res.append(matrix[i2][j])
                i2-=1

            if j1<=j2:
                for j in range(i2,i1-1,-1):
                    # print()
                    res.append(matrix[j][j1])
                j1+=1
        return res