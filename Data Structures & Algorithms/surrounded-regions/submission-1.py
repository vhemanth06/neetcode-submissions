class Solution:
    def solve(self, board: List[List[str]]) -> None:
        sources=[]
        m,n=len(board),len(board[0])
        d=[[0,1],[-1,0],[1,0],[0,-1]]
        for i in range(m):
            if board[i][0]=='O':
                board[i][0]='T'
                sources.append((i,0))
            if board[i][n-1]=='O':
                board[i][n-1]='T'
                sources.append((i,n-1))
        for j in range(n):
            if board[0][j]=='O':
                board[0][j]='T'
                sources.append((0,j))
            if board[m-1][j]=='O':
                board[m-1][j]='T'
                sources.append((m-1,j))
        def bfs(s):
            # visited=set(s)
            q=deque(s)
            while q:
                x,y=q.popleft()
                for dx,dy in d:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<m and 0<=ny<n  and board[nx][ny]=='O':
                        board[nx][ny]='T'
                        q.append((nx,ny))
        bfs(sources)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='T':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'

