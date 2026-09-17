"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hashmap=defaultdict(Node)
        visited=set()
        def dfs(node):
            if not node:
                return 
            hashmap[node]=Node(node.val)
            visited.add(node)
            for n in node.neighbors:
                if n not in visited:
                    dfs(n)
        
        dfs(node)
        for x,y in hashmap.items():
            for n in x.neighbors:
                y.neighbors.append(hashmap[n])
        # dfs2(node)
        return hashmap[node]
