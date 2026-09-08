class ListNode:

    def __init__(self, val, nxt, prev,key):
        self.value, self.next, self.prev ,self.key= val, nxt, prev,key

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap={}
        self.left=ListNode(0,None,None,-1)
        self.right=ListNode(0,None,self.left,-2)
        self.left.next=self.right
        self.cap=capacity
        # self.size=0
    
    def remove(self,Node):
        Node.prev.next=Node.next
        Node.next.prev=Node.prev
    
    def insert(self,Node):
        temp=self.left.next
        self.left.next=Node
        Node.next=temp
        temp.prev=Node
        Node.prev=self.left

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node=self.hashmap[key]
            self.remove(node)
            self.insert(node)
            # node.val=value
            return node.value
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node=self.hashmap[key]
            self.remove(node)
            node.value=value
            self.insert(node)
            
            
        else:
            node=ListNode(value,None,None,key)
            self.hashmap[key]=node
            self.insert(node)
            if len(self.hashmap)>self.cap:
                n=self.right.prev
                self.remove(n)
                # self.size-=1
                del self.hashmap[n.key]
        
        
