"""
Approach1: dfs & recursion
Approach2: stack & while
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = []
        maxdepth = depth = 0
        stack.append([root, depth])
        while stack:
            [node, depth] = stack.pop()
            maxdepth = max(depth, maxdepth)
            if node:
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
        return maxdepth