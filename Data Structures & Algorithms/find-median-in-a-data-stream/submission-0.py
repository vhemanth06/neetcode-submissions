class MedianFinder:

    def __init__(self):
        self.arr=[]
        self.median=-1

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        n=len(self.arr)
        if n%2==0:
            self.median=(self.arr[n//2]+self.arr[n//2-1])/2
        else:
            self.median=self.arr[n//2]

    def findMedian(self) -> float:
        return self.median
        
        