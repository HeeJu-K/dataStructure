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
        self.maxDepth = depth = 1 if root else 0

        def dfs( node, depth):
            if not node : 
                return
            self.maxDepth = max(depth, self.maxDepth)
            if node.left:
                dfs(node.left, depth+1)
            if node.right:
                dfs(node.right, depth+1)
            return

        dfs(root, depth)
        return self.maxDepth