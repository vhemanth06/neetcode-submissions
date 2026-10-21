class Trie:
    def __init__(self):
        self.children={}
        self.isword=False
    
    def insert(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=Trie()
            cur=cur.children[c]
        cur.isword=True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root=Trie()
        for word in wordDict:
            root.insert(word)
        res=[]
        n=len(s)
        def dp(i,temp):
            if i==n:
                res.append(" ".join(temp))
                return
            cur=root
            for j in range(i,n):
                if s[j] not in cur.children:
                    break
                cur=cur.children[s[j]]
                if cur.isword:
                    temp.append(s[i:j+1])
                    dp(j+1,temp)
                    temp.pop()
        dp(0,[])
        return res
