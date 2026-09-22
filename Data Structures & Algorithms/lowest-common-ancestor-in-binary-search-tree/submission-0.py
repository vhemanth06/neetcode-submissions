# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        x,y=p.val,q.val
        cur=root.val
        if cur<min(x,y):
            return self.lowestCommonAncestor(root.right,p,q)
        elif cur>max(x,y):
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
        