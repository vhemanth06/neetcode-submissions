class Solution:
    def isHappy(self, n: int) -> bool:
        def calcu(r):
            x=list(str(r))
            s=0
            for num in x:
                s+=(int(num)**2)
            return s
        s=calcu(n)
        f=set([0,1,2,3,4,5,6,7,8,9])
        while s not in f:
            s=calcu(s)


        return s==1