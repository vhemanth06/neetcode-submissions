# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        x1=[]
        x2=[]
        if root.left:
            x1=self.inorderTraversal(root.left)
        x1.append(root.val)
        if root.right:
            x2=self.inorderTraversal(root.right)
        x1.extend(x2)
        return x1