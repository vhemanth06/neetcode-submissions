class Solution:
    def romanToInt(self, s: str) -> int:
        dic={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        dic2={
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }
        i=0
        n=len(s)
        res=0
        while i<n:
            c=s[i]
            if i+1<n and (c=='I' or c=='X' or c=='C'):
                d=s[i]+s[i+1]
                if d in dic2:
                    res+=dic2[d]
                    i+=2
                else:
                    res+=dic[c]
                    i+=1
            else:
                res+=dic[c]
                i+=1

        return res