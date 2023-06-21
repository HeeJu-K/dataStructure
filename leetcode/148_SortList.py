# 148. Sort List
#Merge Sort
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         #check cases len>1
#         print("here")
#         if not head or not head.next:
#             return head
#         #use slow and fast pointers to locate mid point of the list
#         slow = head
#         fast = head
#         while fast and fast.next:
#             slow = head.next
#             fast = head.next.next
#         mid = slow
#         #divide the list
#         slow.next = None
#         print("head: ", head, "mid: ", mid)
#         #recursion to divide list into individual pieces 
#         left = self.sortList(head)
#         right = self.sortList(mid)
#         #empty node for merging, size doubles on every iterations
#         dummy = ListNode(0, None)
#         cur = dummy
#         while left and right:
#             if left<right:
#                 cur.next = left
#                 left = left.next
#             else:
#                 cur.next = right
#                 right = right.next
#             cur = cur.next
#         #when left or right has remainings
#         cur.next = left or right
#         return dummy.next
        
class Solution:
    def sortList( head):
        # Base Case: If the length of the linked list is less than or equal to 1, then the list is already sorted
        if not head or not head.next:
            return head

        # Split the linked list into two halves using "slow and fast pointer" technique to find the midpoint of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # The midpoint of the linked list is slow.next
        mid = slow.next
        # Set slow.next to None to separate the left and right halves of the linked list
        slow.next = None

        # Recursively sort the left and right halves of the linked list
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge the two sorted halves of the linked list
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        # Append the remaining nodes of the left or right half to the end of the sorted list
        curr.next = left or right

        return dummy.next

if __name__ == '__main__':
    print(Solution.sortList([4,2,1,3]))