# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res=1
        def dfs(Node,maxval):
            if not Node:
                return
            if Node.val>=maxval:
                self.res+=1
            dfs(Node.left,max(maxval,Node.val))
            dfs(Node.right,max(maxval,Node.val))
        dfs(root.left,root.val)
        dfs(root.right,root.val)
        return self.res