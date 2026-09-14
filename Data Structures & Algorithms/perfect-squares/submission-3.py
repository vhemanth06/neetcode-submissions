class Solution:
    def numSquares(self, n: int) -> int:
        memo={0:0}
        def dp(i):
            if i in memo:
                return memo[i]
            res=i
            for j in range(int(i**0.5),0,-1):
                # if j*j>i:
                #     break
                res=min(res,1+dp(i-j*j))
            memo[i]=res
            return res
        return dp(n)
            
