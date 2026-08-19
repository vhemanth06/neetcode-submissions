class MinStack:

    def __init__(self):
        self.s=[]

    def push(self, val: int) -> None:
        if self.s:
            self.s.append([val,min(val,self.s[-1][1])])
        else:
            self.s.append([val,val])

    def pop(self) -> None:
        if self.s:
            self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:







        # print(self.s)
        return self.s[-1][1]
