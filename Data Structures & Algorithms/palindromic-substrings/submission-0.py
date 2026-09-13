class Solution:
    def countSubstrings(self, s: str) -> int:
        res=1
        n=len(s)
        for i in range(n-1):
            l,r=i,i
            while r<n and l>=0 and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            
            l,r=i,i+1
            while r<n and l>=0 and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
        return res