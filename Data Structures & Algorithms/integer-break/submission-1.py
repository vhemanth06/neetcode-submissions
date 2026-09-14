class Solution:
    def integerBreak(self, n: int) -> int:
        cache=[-1]*(n+1)
        cache[1]=1

        def dfs(num):
            if cache[num]!=-1:
                return cache[num]
            res=0 if num==n else num
            for i in range(1,num):
                res=max(res,dfs(i)*dfs(num-i))
            cache[num]=res
            return res
        return dfs(n)