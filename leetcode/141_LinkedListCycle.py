# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Appraoch:
X: distance till start of loop
Y: distance till meeting point
C: length of cycle
fast = X+Y+mC
slow = X+Y+nC
to have two pointers meet, should have 2(X+Y+nC) = X+Y+mC
X+Y = (m-2n)C -> kC
if there is a cycle, there is a meeting point
-> FOLLOW UP
when fast and slow meet for first time, move slow to start and move fast and slow both by one steps (fast at Y, slow at 0)
After X steps, slow reach X and fast react Y+X, which equals kC. 
both kC and X are the start of loop
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
