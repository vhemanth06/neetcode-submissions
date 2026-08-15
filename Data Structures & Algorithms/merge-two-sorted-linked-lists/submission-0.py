# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res=None
        curr1=list1
        curr2=list2
        while curr1 is not None and curr2 is not None:
            if curr1.val<=curr2.val:
                newnode=ListNode(val=curr1.val,next=res)
                res=newnode
                curr1=curr1.next
            else:
                newnode=ListNode(val=curr2.val,next=res)
                res=newnode
                curr2=curr2.next
        while curr1 is not None:
            newnode=ListNode(val=curr1.val,next=res)
            res=newnode
            curr1=curr1.next
        while curr2 is not None:
            newnode=ListNode(val=curr2.val,next=res)
            res=newnode
            curr2=curr2.next
        return self.reverse(res)
    def reverse(self,list1):
        res=None
        curr=list1
        while curr is not None:
            newnode=ListNode(val=curr.val,next=res)
            res=newnode
            curr=curr.next
        return res
        