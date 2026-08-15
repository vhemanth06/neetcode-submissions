# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead=None
        curr=head
        while curr is not None:
            newnode=ListNode(val=curr.val,next=newhead)
            newhead=newnode
            curr=curr.next
        return newhead
