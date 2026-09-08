# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res=False
        def check(Node,subroot):
            if not subroot and not Node:
                return True
            if not subroot or not Node:
                return False
            if Node.val!=subroot.val:
                return False
            return check(Node.left,subroot.left) and check(Node.right,subroot.right)
        def search(Node):
            if not Node:
                return False
            if Node.val==subRoot.val:
                return check(Node,subRoot) or search(Node.left) or search(Node.right)
            else:
                return search(Node.left) or search(Node.right)
        return search(root)
                