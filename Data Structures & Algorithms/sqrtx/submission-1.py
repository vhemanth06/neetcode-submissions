class Solution:
    def mySqrt(self, x: int) -> int:
        def b(l,r):
            if l>r:
                return l-1
            m=(l+r)//2
            if m*m<x:
                return b(m+1,r)
            elif m*m>x:
                return b(l,m-1)
            else:return m
        if x<=1:
            return x
        return b(2,x//2)

        