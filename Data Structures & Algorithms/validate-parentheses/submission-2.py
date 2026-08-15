class Solution:
    def isValid(self, s: str) -> bool:
        m=[]
        for i in s:
            if i==')' and m and m[-1]=='(':
                m.pop()
            elif i=='}' and m and m[-1]=='{':
                m.pop()
            elif i==']' and m and m[-1]=='[':
                m.pop()
            else:
                m.append(i)
        return m==[]
        