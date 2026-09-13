class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        n=len(s)
        hash2=set([
            '10','11','12','13','14','15',
            '16','17','18','19','20','21',
            '22','23','24','25','26'
        ])
        memo=[0]*(n+1)
        memo[n]=1
        def dp(i):
            if memo[i]!=0:
                return memo[i]
            
            x=s[i]
            res=0
            if x!='0':
                res+=dp(i+1)
            if i<n-1:
                y=s[i:i+2]
                if y in hash2:
                    res+=dp(i+2)
            memo[i]=res
            return memo[i]
        return dp(0)

