class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF
        maxint=0x7FFFFFFF
        res=0
        while b!=0:
            temp=((a&b)<<1)&mask
            a=(a^b)&mask
            b=temp
        return a if a<=maxint else ~(a^mask)

