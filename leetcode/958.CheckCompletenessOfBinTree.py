# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### list.pop(0) take O(n) while popleft takes O(1)
### root is a single node, deque takes [] as input
### .popleft() returns Treenode of its own val, left and right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node: # if current node is not null
                q.append(node.left)
                q.append(node.right)
            else: # if current node is null
                while q: # there are still elements in queue
                    if q.popleft(): # there is a non null element in queue
                        return False
        return True 