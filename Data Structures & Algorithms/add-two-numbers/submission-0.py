# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=0
        cur1=l1
        i=0
        while cur1:
            a=cur1.val*(10**(i))+a
            i+=1
            cur1=cur1.next
        b=0
        cur2=l2
        j=0
        while cur2:
            b=cur2.val*(10**(j))+b
            j+=1
            cur2=cur2.next
        x=a+b
        print(x)
        if x==0:
            return ListNode(0)
        head=None
        res=None
        while x!=0:
            rem=x%10
            x=x//10
            node=ListNode(val=rem)
            if head:
                head.next=node
                head=head.next
            else:
                res=node
                head=node

        return res
        