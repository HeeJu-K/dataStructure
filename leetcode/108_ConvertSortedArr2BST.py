"""
Approach: ascending order, have middle one as the root and the rest branching out
height balanced: middle node, and two branch is it.

Note that its sorted in ascending order, thus each left and right subtrees are ascending
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        # mid = n//2
        if not n:
            return None
        
        def buildtree(start, end):
            if start>end: return None

            mid = (start+end)//2
            root = TreeNode(nums[mid])
            root.left = buildtree(start, mid-1)
            root.right = buildtree(mid+1, end)
            return root

        res = buildtree(0, n-1)
        return res