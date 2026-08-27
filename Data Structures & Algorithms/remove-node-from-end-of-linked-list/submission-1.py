# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        l=0
        while cur:
            l+=1
            cur=cur.next
        print(l)
        if l==1:
            return None
        elif l==n:
            return head.next 
        x=l-n-1
        cur2=head
        while x and cur2.next:
            cur2=cur2.next
            x-=1
        if cur2.next and cur2.next.next:
            cur2.next=cur2.next.next
        else:
            cur2.next=None
        return head

    
        
        