class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(s),len(p)
        cache={(-1,-1):True}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if j<0:
                return False
            if i<0:
                if p[j]=='*':
                    return dfs(i,j-2)
                return False
            if p[j]=='*':
                zero=dfs(i,j-2)
                match= s[i]==p[j-1] or p[j-1]=='.'
                cache[(i,j)]= (match and dfs(i-1,j)) or zero
                return cache[(i,j)]
            if s[i]==p[j] or p[j]=='.':
                cache[(i,j)]= dfs(i-1,j-1)
                return cache[(i,j)]
            cache[(i,j)]= False
            return cache[(i,j)]
        return dfs(m-1,n-1)