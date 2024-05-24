"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


TC: if top-down, O(N^2*logN)
    if bottom - top, O(N^2)
SC: constant SC used for each recursion, logN times for recusion stack
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def divide(x, y, length): # x, y indicates coordinates of top left item
            if length == 1:
                return Node(grid[x][y], 1, None, None, None, None)
            topLeft = divide(x, y, length//2)
            topRight = divide(x, y+length//2, length//2)
            bottomLeft = divide(x+length//2, y, length//2)
            bottomRight = divide(x+length//2, y+length//2, length//2)
            if topLeft.val == topRight.val == bottomLeft.val == bottomRight.val and topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf:
                return Node(topLeft.val, 1, None, None, None, None)
            else:
                return Node(0, 0, topLeft, topRight, bottomLeft, bottomRight)
        return divide(0,0,len(grid))