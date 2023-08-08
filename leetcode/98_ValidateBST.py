"""
Approach: recursion
left subtree < cur node
right subtree > cur node
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkValid(node, left, right):
            if not node: return True
            if left <= node.val or right >= node.val:
                return False
            return checkValid(node.left, node.val, right) and checkValid(node.right, left, node.val)

        return checkValid(root, float("inf"), float("-inf"))