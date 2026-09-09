class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2)>len(str1):
            str1,str2=str2,str1
        m,n=len(str1),len(str2)
        for i in range(n,0,-1):
            g=str2[0:i]
            l=len(g)
            if m%l==0 and n%l==0:
                s1=g*(m//l)
                s2=g*(n//l)
                if str1==s1 and str2==s2:
                    return g
        return ""