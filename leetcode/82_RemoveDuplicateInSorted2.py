# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

### make another listnode that next is head, to avoid cases which first element of the head is already a duplicate so it has to be eliminated. In such an edge case head have to be dealt with bu itself, as we are returning the head node of the duplicated-removed listnode
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result.next = head
        cur = result

        while head and head.next:
            # print("CUR--", cur)
            # print("HEAD--", head)
            # print("RESULT--", result)
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                cur.next = head
            else:
                cur = cur.next
                head = head.next
            
        return result.next