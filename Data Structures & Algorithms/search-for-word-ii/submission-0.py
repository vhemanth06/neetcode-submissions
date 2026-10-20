class TrieNode:
    def __init__(self):
        self.children={}
        self.endswith=False

    def insert(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.endswith=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie=TrieNode()
        for word in words:
            trie.insert(word)
        m,n=len(board),len(board[0])
        res,visit=set(),set()
        def dfs(r,c,node,word):
            if r>=m or r<0 or c>=n or c<0 or (r,c) in visit or board[r][c] not in node.children:
                return
            
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.endswith:
                res.add(word)
            
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visit.remove((r,c))


        for i in range(m):
            for j in range(n):
                dfs(i,j,trie,"")
        return list(res)