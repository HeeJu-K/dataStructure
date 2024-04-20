# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
DFS
store distance to each leaf on each node with DFS. 
DFS to smallest subtree. store leaf node in arrays. concat left and right arrays on each node
"""
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        pairs = 0

        def dfs(root):
            nonlocal pairs
            # no node
            if not root:
                return [] # return empty array to make it iterable
            # leaf node
            if not root.left and not root.right:
                return [1] # from root perspective, distance to left leaf or right leaf is 1
            left = dfs(root.left)
            right = dfs(root.right)
            for l in left:
                for r in right:
                    if l+r <= distance:
                        pairs += 1
            return [d+1 for d in left+right]
        dfs(root)
        return pairs