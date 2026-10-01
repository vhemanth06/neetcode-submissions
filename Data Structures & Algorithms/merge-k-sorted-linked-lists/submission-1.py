# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # def __lt__(self,other):
    #     return self.val<other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        minheap=[]
        n=len(lists)
        for i in range(n):
            if lists[i]:
                cur=lists[i]
                heapq.heappush(minheap,(cur.val,i,cur))
        dummy=ListNode()
        temp=dummy
        while minheap:
            _,i,c=heapq.heappop(minheap)
            temp.next=c
            temp=temp.next
            if c.next:
                heapq.heappush(minheap,(c.next.val,i,c.next))
        return dummy.next

       
