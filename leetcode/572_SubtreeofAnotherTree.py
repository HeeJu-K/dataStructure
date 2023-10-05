"""
Approach:
Tip!: Notice that subtree includes all of the descendents, so we are not only looking for its direct childs
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return root == subRoot
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, node, ref):
        if node and ref:
            return node.val == ref.val and self.isSameTree(node.left, ref.left) and self.isSameTree(node.right, ref.right)
        return node == ref