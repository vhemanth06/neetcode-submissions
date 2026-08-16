class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        l=len(tokens)
        for tok in tokens:
            if tok=="+":
                x1=s.pop()
                x2=s.pop()
                s.append(x1+x2)
            elif tok=="-":
                x1=s.pop()
                x2=s.pop()
                s.append(x2-x1)
            elif tok=="*":
                x1=s.pop()
                x2=s.pop()
                s.append(x2*x1)
            elif tok=="/":
                x1=s.pop()
                x2=s.pop()
                s.append(int(x2/x1))
            else:
                s.append(int(tok))
        return s[0]
