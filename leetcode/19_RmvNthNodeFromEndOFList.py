"""
Approach: 
Two pointers:
nth node from the end == len - n
If fast pointer is starting from nth node from start, slow pointer will advance len - n
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = prev = head
        for _ in range (n):
            fast = fast.next
        
        if not fast: return head.next
        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        if slow and slow.next:
            slow.next = slow.next.next 
        return head
