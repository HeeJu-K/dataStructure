"""
Maintain a monotonic stack
BST: once a number is greater, its left subtree need not be considered

the stack should be appended in decreasing order
if non decreasing elem is encountered, pop the elem and set it as minLim
O(n), O(n)
"""
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        maxheap = []
        minLim = float("-inf")
        for item in preorder:
            if not maxheap:
                maxheap.append(item)
            else:
                if maxheap[-1]>item and item > minLim:
                    maxheap.append(item)
                else:
                    if item < minLim : 
                        return False
                    minLim = maxheap.pop()
                    while maxheap and maxheap[-1] < item:
                        minLim = maxheap.pop()
                    maxheap.append(item)
                    
        return True