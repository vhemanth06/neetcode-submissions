from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.hashcount=defaultdict(int)
        self.maping=defaultdict(list)
        self.maxcount=0

    def push(self, val: int) -> None:
        self.hashcount[val]+=1
        self.maping[self.hashcount[val]].append(val)
        self.maxcount=max(self.hashcount[val],self.maxcount)

    def pop(self) -> int:
        x=self.maping[self.maxcount].pop()
        if not self.maping[self.maxcount]:
            self.maxcount-=1
        self.hashcount[x]-=1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()