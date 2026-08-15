# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def b(l,r):
            m=(l+r)//2
            if guess(m)==-1:
                return b(l,m-1)
            elif guess(m)==1:
                return b(m+1,r)
            else:return m
        return b(1,n)
        