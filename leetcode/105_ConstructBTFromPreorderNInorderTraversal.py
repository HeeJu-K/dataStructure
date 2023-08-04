"""
Approach: Partition
pre-order visits the root first, in-order visites the left - root - right
thus pre-order will tell you the root node, everything in in-order before that root node is left subtree and after that is right subtree
PARTITION
find the root node from pre-order tree. find the index of that root node. in preorder, root node to root node + index will be right subtree. after that will be left subtree. Recursively partition
 and build the tree
 """
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # print("start", preorder, inorder)
        if not preorder : return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return root