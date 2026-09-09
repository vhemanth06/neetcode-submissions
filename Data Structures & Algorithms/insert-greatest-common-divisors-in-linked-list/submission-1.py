# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        def findgcd(num1,num2):
            if num2>num1:
                num1,num2=num2,num1
            while num2:
                num1,num2=num2,num1%num2
            return num1
        def insert(node,left,right):
            left.next=node
            node.next=right
        cur=head.next
        prev=head
        while cur:
            node=ListNode(findgcd(cur.val,prev.val),None)
            insert(node,prev,cur)
            prev,cur=cur,cur.next
        return head



        