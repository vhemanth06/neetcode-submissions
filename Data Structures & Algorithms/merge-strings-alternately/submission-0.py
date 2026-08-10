class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1=0
        p2=0
        l1=len(word1)
        l2=len(word2)
        r=""
        while p1<l1 or p2<l2:
            if p1<l1:
                r+=word1[p1]
                p1+=1
            if p2<l2:
                r+=word2[p2]
                p2+=1
        return r

        