class StockSpanner:

    def __init__(self):
        self.s=[]

    def next(self, price: int) -> int:
        x=self.s.copy()
        res=1
        while x and x[-1]<=price:
            x.pop()
            res+=1
        self.s.append(price)
        return res 


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)