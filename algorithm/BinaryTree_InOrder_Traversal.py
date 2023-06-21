# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        itr = []
        if root: 
            if root.left:
                #call inorderTraversal again with root.left as parameter, root.left becomes the new root node, it's not the root node of the tree
                itr += self.inorderTraversal(root.left) 

            itr.append(root.val)

            if root.right:
                itr += self.inorderTraversal(root.right)
        
        return itr