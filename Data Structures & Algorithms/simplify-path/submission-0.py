class Solution:
    def simplifyPath(self, path: str) -> str:
        
        x=path.split("/")
        sta=[]
        print(x)
        for s in x:
            if s=="..":
                if sta:
                    sta.pop()
            elif s=="." or s=="":
                continue
            else:
                sta.append(s)
        return "/"+"/".join(sta)
        