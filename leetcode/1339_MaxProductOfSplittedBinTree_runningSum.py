# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### In python, once a global variable is modified in the function, it is treated as local variable. Thus, when calling a variable defined outside from an inside function, should not change the value of it 
class Solution:
    tree_sum = 0
    half_sum = 0
    result = 0
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.getSum(root)
        self.half_sum = self.tree_sum/2
        self.runningSum(root)
        return self.result % (10**9 + 7)

    def getSum(self, node):
        if node:
            self.tree_sum += node.val
            self.getSum(node.left)
            self.getSum(node.right)
        
    # running sum returns sums of the subtree from the lower left end. 
    # returns sums of left subtree and right subtree in turns
    # this case every subtree is compared for the max sum
    def runningSum(self, node):
        if node:
            subtree_sum = node.val
            subtree_sum += self.runningSum(node.left)
            subtree_sum += self.runningSum(node.right)
            self.result = max(self.result, subtree_sum*(self.tree_sum - subtree_sum))
            return subtree_sum
        else: return 0