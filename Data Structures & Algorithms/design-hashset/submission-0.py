class MyHashSet:

    def __init__(self):
        self.arr=[[]]*100


        

    def add(self, key: int) -> None:
        x=key%100
        if not self.contains(key):
            self.arr[x].append(key)
        

    def remove(self, key: int) -> None:
        x=key%100
        try:
            self.arr[x].remove(key)
        except ValueError:
            pass
        

    def contains(self, key: int) -> bool:
        x=key%100
        for num in self.arr[x]:
            if num==key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)