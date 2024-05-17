# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
last idx of postorder is root
postorder always returns rightmost subtrees at last
should always subdivide into sections & specify left and right borders to avoid duplicates
"""

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hm = {}
        for idx, val in enumerate(inorder):
            hm[val] = idx
        
        def getSubtree(left, right):
            if left>right: 
                return None
            root = TreeNode(postorder.pop())
            rootIdx = hm[root.val]
            root.right = getSubtree(rootIdx+1, right)
            root.left = getSubtree(left, rootIdx-1 )
            return root
        
        return getSubtree(0, len(inorder)-1)