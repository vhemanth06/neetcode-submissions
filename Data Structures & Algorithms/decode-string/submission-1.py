class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        sl=list(s)
        i=0
        while i<len(sl):
            # print(stack)
            l=sl[i]
            if l.isdigit():
                num=''
                while sl[i].isdigit():
                    num+=sl[i]
                    i+=1
                stack.append(int(num))
            
            elif l=='[':
                i+=1
                continue
            elif l==']':
                # x=stack.pop()
                t=''
                while stack and not isinstance(stack[-1], int):
                    t=stack.pop()+t
                n=stack.pop()
                stack.append(t*n)
                i+=1
            else:
                stack.append(l)
                i+=1
        
        return "".join(stack)
