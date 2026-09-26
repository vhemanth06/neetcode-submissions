class CountSquares:

    def __init__(self):
        self.hashcount=defaultdict(int)
        self.arr=[]

    def add(self, point: List[int]) -> None:
        self.hashcount[tuple(point)]+=1
        self.arr.append(point)

    def count(self, point: List[int]) -> int:
        px,py=point
        res=0
        for x,y in self.arr:
            if abs(x-px)!=abs(y-py) or (x==px or y==py):
                continue
            res+=(self.hashcount[(x,py)])*(self.hashcount[(px,y)])
        return res
