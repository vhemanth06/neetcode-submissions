# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr=[]
        cur=head
        while cur:
            arr.append(cur)
            cur=cur.next
        left=left-1
        right-=1
        print(arr)
        arr[left:right+1] = reversed(arr[left:right+1])
        print(arr)
        for i in range(len(arr)-1):
            arr[i].next=arr[i+1]
        arr[-1].next = None
        return arr[0]
        
        
