# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        # prev,cur=dummy,head
        startprev,start=dummy,head
        # counter=0
        while start:
            end=start
            for _ in range(k):
                if end is None:
                    return dummy.next
                end=end.next
            self.reverse(startprev,start,end)
            startprev=start
            start=end
            # counter+=1
            # prev=cur
            # cur=cur.next
            
            # if counter==k:
                
            #     startprev=prev
            #     start=cur
            #     counter=0
            
        return dummy.next

    def reverse(self,startprev,start,endnext):
        
        prev,cur=None,start
        while cur!=endnext:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        startprev.next=prev
        start.next=endnext
        
