# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
brute force 
for every node in A check if existent in B or not by iterating
TC: O(M+N)

set
TC:O(M+N)
SPACE: O(max(M,N))

two pointer
longer: length of M
M-C |common| C
N-C |common| C
shorter: length of N

when shorter reaches end first, longer still has M-N till end
make shorter start from longer again, M-C - (M-N) -> N-C
if longer reached end and start from shorter, they will meet at same node
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA
        