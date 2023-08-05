"""
Approach: partition
Assign 1 to n as root by turns
build trees from its left and right subtrees each time, chaning root within the subtrees as well
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int):
        def generate(start, end):
            if start>end: return [None] # [None] is providing empty tree
            
            res = [] #for every node created, res is being appended, but the big for loop in the main recursion will only contain final results
            for i in range(start, end+1):
                left = generate(start, i-1)
                right = generate(i+1, end)

                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res

        return generate(1, n) if n else []