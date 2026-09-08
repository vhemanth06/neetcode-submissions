class MyCircularQueue:

    def __init__(self, k: int):
        self.arr=[-1]*k
        self.point=0
        self.count=k
        self.rear=-1

    def enQueue(self, value: int) -> bool:
        # print(self.arr)
        for i in range(len(self.arr)):
            if self.arr[i]==-1:
                self.arr[i]=value
                self.count-=1
                self.rear=i
                # print('after inset')
                # print(self.arr)
                # print(self.point)
                return True
        return False

    def deQueue(self) -> bool:
        if self.arr[self.point]==-1:
            return False
        self.arr[self.point]=-1
        self.count+=1
        self.point+=1
        if self.point==len(self.arr) or self.isEmpty():
            self.point=0
        
        return True

    def Front(self) -> int:
        return self.arr[self.point]

    def Rear(self) -> int:
        return self.arr[self.rear] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return True if self.count==len(self.arr) else False


    def isFull(self) -> bool:
        return True if self.count==0 else False
    
    

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()