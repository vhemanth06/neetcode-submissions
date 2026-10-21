class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        # self.res=0
        cache=defaultdict(int)
        
        def dp(i,k):
            if k==n:
                
                return 1
            if i==m:
                return 0
            if (i,k) in cache:
                return cache[(i,k)]
            res=0
            if s[i]==t[k]:
                res+=dp(i+1,k+1)
            res+=dp(i+1,k)
            cache[(i,k)]=res
            return res
        # dp(0,0)
        return dp(0,0)
