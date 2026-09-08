class MyCircularQueue:
    def __init__(self, k: int):
        self.data=[0]*k
        self.size=0
        self.cap=k
        self.head=0
        self.tail=-1
    def enQueue(self, value: int) -> bool:
        if self.isFull() :
            return False
        self.tail=(self.tail+1)%self.cap
        self.data[self.tail]=value
        self.size+=1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # self.data[self.head]=0
        self.head=(self.head+1)%self.cap
        self.size-=1
        return True
    def Front(self) -> int:
        return self.data[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        print(self.data)
        return self.data[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()