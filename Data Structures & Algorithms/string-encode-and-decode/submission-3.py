class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for st in strs:
            x=len(st)
            s+=(str(x)+"#"+st)
        # print(s)
        return s

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i=0
        res=[]
        dig=''
        while i<len(s):
            if s[i].isdigit():
                dig+=s[i]
                i+=1
            elif s[i]=="#":
                d=int(dig)
                res.append(s[i+1:i+1+d])
                i+=(1+d)
                dig=""
        return res