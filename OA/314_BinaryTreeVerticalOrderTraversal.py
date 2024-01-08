# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        # create a list of tuples
        q = deque([(root, 0)])
        res = []
        while q:
            node, col = q.popleft()
            if node:
                cols[col].append(node.val)
                if node.left:
                    q.append((node.left, col-1))
                if node.right:
                    q.append((node.right, col+1))
        
        l = len(cols.keys())
        for i in range(-l+1, l):
            if i in cols.keys():
                res.append(cols[i])
        return res
