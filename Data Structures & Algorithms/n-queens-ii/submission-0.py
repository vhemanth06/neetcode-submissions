class Solution:
    def totalNQueens(self, n: int) -> int:
    
        col=set()
        posdiag=set()
        negdiag=set()
        self.res=0

        def backtrack(r):
            if r==n:
                self.res+=1
                return

            for c in range(n):
                if c not in col and r+c not in posdiag and r-c not in negdiag:
                    col.add(c)
                    posdiag.add(r+c)
                    negdiag.add(r-c)
                    backtrack(r+1)
                    col.remove(c)
                    posdiag.remove(r+c)
                    negdiag.remove(r-c)
        backtrack(0)
        return self.res

