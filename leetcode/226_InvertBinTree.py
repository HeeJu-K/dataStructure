"""
Approach 1: Recursion, store left tree, right tree then invert
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### Approach 1: call a function
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         return self.traverseTree(root)
#     def traverseTree(self, node):
#         if not node:
#             return None
#         tree = TreeNode()
#         tree.val = node.val
#         if node.left:
#             tree.right = self.traverseTree(node.left)
#         if node.right:
#             tree.left = self.traverseTree(node.right)
#         return tree

### Approach 2: Swap left and right w/o creating new tree
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root