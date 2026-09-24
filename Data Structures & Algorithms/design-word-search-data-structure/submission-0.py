class TrieNode:
    def __init__(self):
        self.children={}
        self.endwith=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.endwith=True

    def search(self, word: str) -> bool:
        def treesearch(node,s):
            if not s:
                return node.endwith
            if s[0]=='.':
                for child in node.children.values():
                    if treesearch(child,s[1:]):
                        return True
                return False
            else:
                if s[0] in node.children:
                    return treesearch(node.children[s[0]],s[1:])
                else:
                    return False
        return treesearch(self.root,word)

        
