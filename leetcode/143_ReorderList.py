"""
Approach: Find Mid node, cut half, reverse right halve, join the two lists

Find mid node: Fast and Slow pointers
Reverse List: Problem 206
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid node
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # split the lists to right half (right) and left half (head)
        list2 = slow.next
        slow.next = None

        cur2 = self.reverseList(list2) # reverse the right half
        cur1 = head # in here, cur1 is only a reference towards head, changing cur1 will not modify head itself
        while cur1 and cur2:            
            tmp1, tmp2 = cur1.next, cur2.next # store reference to next node for next iteration
            cur1.next = cur2 # connect 1st elem in cur1 to 1st elem in cur2
            cur2.next = tmp1 # connect 1st elem in cur2 to 2nd element in cur1
            cur1, cur2 = tmp1, tmp2 # update the reference

            
    def reverseList(self, head):
        new_list = None # the new reversed list
        cur = new_list # the pointer to the new_list
        while head:
            next_node = head.next # store the head for next iteration
            head.next = cur # append the new_list after the current head
            cur = head # move the pointer of reversed list to have access to current node
            head = next_node # update the head for next iteration
        return cur # return the pointer to the reversed list
    
