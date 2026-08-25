class Solution:
    def countBits(self, n: int) -> List[int]:
        def count1s(x):
            res=0
            for i in range(32):
                if ((1<<i) & x):
                    res+=1
            return res
        return [count1s(x) for x in range(n+1)]
        