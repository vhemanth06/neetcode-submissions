class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        x1=1
        x2=2

        res=0
        for i in range(3,n+1):
            res=x1+x2
            x1,x2=x2,res
        return res