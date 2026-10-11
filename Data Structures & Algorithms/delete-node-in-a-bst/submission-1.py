# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        val=root.val
        if key<val:
            root.left=self.deleteNode(root.left,key)
        elif key>val:
            root.right=self.deleteNode(root.right,key)
        else:
            if not root.left:
                root=root.right
            elif not root.right:
                root=root.left
            else:
                cur=root.right
                prev=root
                while cur.left:
                    prev=cur
                    cur=cur.left
                root.val=cur.val
                if prev==root:
                    prev.right=cur.right
                else:
                    
                    prev.left=cur.right
                    
        return root
        