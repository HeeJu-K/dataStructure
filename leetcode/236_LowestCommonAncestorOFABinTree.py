"""
Case1: node A is below node B
Case2: node A and node B are in different subtrees
Approach1: Record heights of trees
Approach2: Mark subtree as True is one node is found, get height
Approach3: return root if one node is found, if both l and r are not none, LCA is found
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # left = right = False
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # if not root: return root
        if not root or root.val == p.val or root.val == q.val:
            return root
        
        left =  self.lowestCommonAncestor(root.left, p, q)
        right =  self.lowestCommonAncestor(root.right, p, q)        
        
        if left and right:
            return root
        return left or right # return the found node