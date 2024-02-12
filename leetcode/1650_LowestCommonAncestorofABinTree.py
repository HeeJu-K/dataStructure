"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
# O(n), O(n)
# class Solution:
#     def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
#         seen = set()
#         while p:
#             seen.add(p.val)
#             p = p.parent
#         while q and q.val not in seen:
#             q = q.parent
#         return q
    
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

put parents in a set, once seen, return the node
O(height of tree), time and space
O(V+E), O(1): find root, bfs from root
O(n), O(1): find 
"""

class Solution:
    def getDepth(self, p:'Node') -> int:
        d = 0
        while p.parent:
            p = p.parent
            d += 1
        return d
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        depthP = self.getDepth(p)
        depthQ = self.getDepth(q)

        a = p
        b = q
        
        for _ in range (depthP - depthQ):
            a = a.parent
        for _ in range (depthQ - depthP):
            b = b.parent
        while a != b :
            a = a.parent
            b = b.parent
        return a
       