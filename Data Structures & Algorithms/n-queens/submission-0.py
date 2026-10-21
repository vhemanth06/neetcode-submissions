class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for _ in range(n)]
        res=[]

        col=set()
        posdiag=set()
        negdiag=set()



        def backtrack(r):
            if r==n:
                res.append(["".join(x) for x in board])
                return
            
            for c in range(n):
                if c not in col and r+c not in posdiag and r-c not in negdiag:
                    col.add(c)
                    posdiag.add(r+c)
                    negdiag.add(r-c)
                    board[r][c]='Q'
                    backtrack(r+1)
                    board[r][c]="."
                    col.remove(c)
                    posdiag.remove(r+c)
                    negdiag.remove(r-c)
        
        backtrack(0)
        return res
    

