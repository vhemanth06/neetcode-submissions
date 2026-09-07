"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        hashmap={}
        cur=head

        while cur:
            copy=Node(cur.val)
            hashmap[cur]=copy
            cur=cur.next
        
        cur=head
        while cur:
            copy=hashmap[cur]
            if cur.next is not None:
                copy.next=hashmap[cur.next]
            if cur.random is not None:
                copy.random=hashmap[cur.random]
            cur=cur.next
        return hashmap[head]