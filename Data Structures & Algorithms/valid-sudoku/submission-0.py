class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkrow(board):
            for i in range(9):
                s=set()
                for j in range(9):
                    x=board[i][j]
                    if x!=".":
                        if x in s:
                            return False
                        else:
                            s.add(x)
            return True
        
        def checkcol(board):
            for j in range(9):
                s=set()
                for i in range(9):
                    x=board[i][j]
                    if x!=".":
                        if x in s:
                            return False
                        else:
                            s.add(x)
            return True
        def checkbox(board,rend,cend):
            s=set()
            for i in range(rend,rend+3):
                for j in range(cend,cend+3):
                    x=board[i][j]
                    if x!=".":
                        if x in s:
                            return False
                        else:
                            s.add(x)
            return True
        def checkallbox(board):
            for i in range(0,9,3):
                for j in range(0,9,3):
                    if not checkbox(board,i,j):
                        return False
            return True
        return checkrow(board) and checkcol(board) and checkallbox(board)
        
