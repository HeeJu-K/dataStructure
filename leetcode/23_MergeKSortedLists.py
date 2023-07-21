from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ### The Optional annotation in python indicates that the return value can either be of type ListNode or None, nothing else

        if len(lists) == 0 :
            return None
        
        mergedList = []
        mergedTmp = []

        for i in range (0,len(lists),2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1<len(lists) else []
            mergedTmp = self.mergeList(l1, l2)
            mergedList = self.mergeList(mergedList , mergedTmp)

        return mergedList

    def mergeList(self, l1, l2):
        ### make dummy for the sake of first node
        dummy = ListNode() 
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
        

        

if __name__ == '__main__':
    print(Solution().mergeKLists([[1,4,5],[1,3,4],[2,6]]))