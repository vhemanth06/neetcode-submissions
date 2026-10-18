class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]
        # self.median=-1

    def addNum(self, num: int) -> None:
        if self.large and num>self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-num)
        m,n=len(self.small),len(self.large)
        if m>n+1:
            x=-heapq.heappop(self.small)
            heapq.heappush(self.large,x)
        elif n>m+1:
            x=heapq.heappop(self.large)
            heapq.heappush(self.small,-x)

    def findMedian(self) -> float:
        m,n=len(self.small),len(self.large)
        if m==n:
            return (self.large[0]-self.small[0])/2
        elif m>n:
            return -self.small[0]
        else:
            return self.large[0]
        
        