# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### In python, once a global variable is modified in the function, it is treated as local variable. Thus, when calling a variable defined outside from an inside function, should not change the value of it 
class Solution:
    
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        max_tree = []
        tree_sum = 0
        def dfs(node):
            if not node:
                return 0
            tree_sum = node.val + dfs(node.left) + dfs(node.right)
            max_tree.append(tree_sum)
            return tree_sum
        total_sum = dfs(root)
        return max( sub_sum*(total_sum - sub_sum)for sub_sum in max_tree) %( 10**9+7)

