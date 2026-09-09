# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur and cur.next:
            gcd=math.gcd(cur.val,cur.next.val)
            node=ListNode(gcd,cur.next)
            cur.next=node
            cur=node.next
        return head
        