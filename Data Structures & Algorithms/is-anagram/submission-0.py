class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1={}
        m2={}
        l1=len(s)
        l2=len(t)
        if l1!=l2:
            return False
        for i in range(l1):
            if s[i] in m1:
                m1[s[i]]+=1
            else:
                m1[s[i]]=1
            if t[i] in m2:
                m2[t[i]]+=1
            else:
                m2[t[i]]=1
        return m1==m2
        
        