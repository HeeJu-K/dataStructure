# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
before M, length of cycle N
fast, slow
M+aN+x = 2(M+bN+x)
(a-2b)N = x + M = pos
I wish to find the length of M
M = kN - x, where N is the length of cycle
the length of remaining cycle from x to start, is the length of start to M
"""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: break
        
        if fast is None or fast.next is None:
            return None
        
        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
        