class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        i=0
        for j in range(len(t)):
            if i<len(s) and t[j]==s[i]:
                i+=1
       
        return True if i==len(s) else False