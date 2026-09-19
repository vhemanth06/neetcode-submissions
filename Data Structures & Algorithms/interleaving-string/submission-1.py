class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,l=len(s1),len(s2),len(s3)
        if not m+n==l:
            return False
        cache={}
        def dp(i,j,k):
            if i<0 or j<0:
                if s2[:j+1]==s3[:k+1] or s1[:i+1]==s3[:k+1]:
                    return True
                else:
                    return False
            if (i,j) in cache:
                return cache[(i,j)]

            res=False
            if s1[i]==s3[k]:
                res=res or dp(i-1,j,k-1)
            if s2[j]==s3[k]:
                res=res or dp(i,j-1,k-1)
            if not (s1[i]==s3[k]  or s2[j]==s3[k]):
                cache[(i,j)]= False
            else:
                cache[(i,j)]= res
            return cache[(i,j)]
        return dp(m-1,n-1,l-1)