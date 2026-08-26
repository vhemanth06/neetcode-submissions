class Solution:
    def reverse(self, x: int) -> int:
        intmax=0x7FFFFFFF
        if x==0:
            return 0
        m=int(x/abs(x))
        x=abs(x)
        res=0
        while x!=0:
            a=x%10
            x=x//10
            res=res*10+a
            if res>intmax:
                return 0
        return res*m
            