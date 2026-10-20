class TrieNode:
    def __init__(self):
        self.children={}
        self.isword=False

    def insert(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.isword=True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root=TrieNode()
        for word in dictionary:
            root.insert(word)
        # res=-1
        n=len(s)
        cache={}
        def dp(j):
            if j==n:
                return 0
            if j in cache:
                return cache[j]
            res=1+dp(j+1)
            cur=root
            for i in range(j,n):
                c=s[i]
                if c not in cur.children:
                    break
                cur=cur.children[c]
                if cur.isword:
                    res=min(res,dp(i+1))
            cache[j]=res
            return res
        return dp(0)
