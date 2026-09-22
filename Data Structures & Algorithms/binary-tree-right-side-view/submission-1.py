# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        q=deque()
        q.append(root)
        while q:
            n=len(q)
            res.append(q[-1].val)
            for _ in range(n):
                x=q.popleft()
                if x.left :
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
        return res