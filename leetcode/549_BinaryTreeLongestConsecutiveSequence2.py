# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
parent node and child node +- 1
iterate via dfs recursion. for each node get longest subsequence of left side and right side
return max_len
O(V+E), O(N)

either ONLY increase or decrease. in one path, only consider increasing path or decreasing path, not a mix of two
for the mixture case, this code might work
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        max_len = 0
    
        def dfs(node):
            left, right = 1, 1
            nonlocal max_len
            
            if not node: return left, right
            
            if node.left:
                left, right = dfs(node.left)
                if node.left.val == node.val + 1 or node.left.val == node.val - 1:
                    left += 1
                    print("here", left)
                
            if node.right:
                l, r = dfs(node.right)
                if node.right.val == node.val + 1 or node.right.val == node.val - 1:
                    right = max(right, r+1)
                    left = max(left, l)
                    print("there", right)
                else: right = 1
                
            print("node.val", node.val, left, right)
            max_len = max(left+right-1, max_len)
            return left, right
        dfs(root)
        return max_len

"""
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        max_len = 0
    
        def dfs(node):
            inc, dec = 1, 1
            nonlocal max_len
            
            if not node: return inc, dec
            #since its bottom - top, inc are always child + 1 and dec are alwats child - 1 
            if node.left:
                left = dfs(node.left) 
                if node.left.val + 1 == node.val:
                    inc = left[0] + 1
                elif node.left.val - 1 == node.val:
                    dec = left[1] + 1
                
            if node.right:
                right = dfs(node.right)
                if node.right.val + 1 == node.val:
                    inc = max(inc, right[0]+1)
                elif node.right.val - 1 == node.val:
                    dec = max(dec, right[1]+1)
        
            max_len = max(inc+dec-1, max_len)
            return inc, dec
        dfs(root)
        return max_len