# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index={val: i for i, val in enumerate(inorder)}
        self.preind=0
        def func(l,r):
            if l>r:
                return None
            rootval=preorder[self.preind]
            self.preind+=1
            root=TreeNode(rootval)
            mid=index[rootval]
            root.left=func(l,mid-1)
            root.right=func(mid+1,r)
            return root
        return func(0,len(preorder)-1)