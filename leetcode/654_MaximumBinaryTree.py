# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
O(n^2), can be further optimized with bin search
find max and its index
create left subtree with left subarray
create right subtree with right subarray
"""
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def findMax(arr):
            maxIdx, maxNum = 0, 0
            for i, num in enumerate(arr):
                if num>maxNum:
                    maxIdx, maxNum = i, num
            return maxIdx, maxNum
        def constructTree(arr):
            if not len(arr): return None
            maxIdx, maxNum = findMax(arr)
            root = TreeNode(maxNum)
            root.left = constructTree( arr[:maxIdx])
            root.right = constructTree( arr[maxIdx+1:])
            return root
        
        return constructTree(nums)
