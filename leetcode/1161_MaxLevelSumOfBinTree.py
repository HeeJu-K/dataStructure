# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        # stack = [] #level, sum
        max_sum = float(-inf)
        result = 0
        level = 0

        while queue:
            level += 1
            level_sum = 0

            for _ in range(len(queue)): 
                node = queue.popleft()
                if node:
                    level_sum += node.val
                    
                #there are nodes with null value that has children
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if level_sum > max_sum:
                result = level
                max_sum = level_sum

        return result