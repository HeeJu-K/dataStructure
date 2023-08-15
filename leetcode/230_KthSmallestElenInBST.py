"""
Approach: DFS, Stack
In order traversal gives order of sorted from smallest elem. 
Use Stack to store visited nodes from root, once furthest left is reached, pop and decrement k

Follow up:

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.stack = []
        self.inorder(root)
        # print("end", self.stack)
        return self.stack[k-1]

    def inorder(self, node):
        if node is None: return 

        self.inorder(node.left)
        self.stack.append(node.val)
        self.k-=1
        # in here, we found the leftmost element
        if self.k == 0: return # found
        # here we have seen smallest i nodes where i<k, now see right to check for missing smaller values before going back to the parent node
        self.inorder(node.right)