"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) :
        m=len(grid)
        ones=0
        for i in range(m):
            for j in range(m):
                if grid[i][j]==1:
                    ones+=1
        if ones==(m**2) or ones==0:
            return Node(val=bool(grid[0][0]),isLeaf=True)
        else:
            x=Node(val=True)
            x.topLeft=self.construct([row[:m//2] for row in grid[:m//2]])
            x.bottomRight=self.construct([row[m//2:] for row in grid[m//2:]])
            x.topRight=self.construct([row[m//2:] for row in grid[:m//2]])
            x.bottomLeft=self.construct([row[:m//2] for row in grid[m//2:]])
            return x