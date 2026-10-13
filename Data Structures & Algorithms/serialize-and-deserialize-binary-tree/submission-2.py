# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        pre=[]
        # ino=[]
        def preorder(node):
            
            if not node:
                pre.append("#")
                return
            pre.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        
        # # inorder(root)
        # print(pre)
        return ",".join(pre)
        


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val=data.split(',')
        self.i=0
        def dfs():
            # nonlocal i
            if val[self.i]=='#':
                self.i+=1
                return None
            root=TreeNode(int(val[self.i]))
            self.i+=1
            root.left=dfs()
            root.right=dfs()
            return root
        return dfs()
