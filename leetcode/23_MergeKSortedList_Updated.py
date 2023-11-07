"""
Approach: Divide and Conquer, merge two lists each time 
Time Complexity: K lists & N nodes -> Nlog2K 
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = len(lists)
        if l == 0:
            return None
        # 5 lists A B C D E
        # AB CD E interval 2
        # ABCD E interval 4
        
        interval = 1 # start with skipping one list at a time
        while interval < l:
            for i in range (0, l-interval, interval*2):
                lists[i] = self.mergeTwo(lists[i], lists[i+interval])
            interval *= 2
        return lists[0]
    def mergeTwo(self, list1, list2):
        # print("here ", list1, list2)
        head = dummy = ListNode(0)
        while list1 and list2:
            if list1.val > list2.val:
                dummy.next = list2
                list2 = list2.next
            else:
                dummy.next = list1
                list1 = list1.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2
        # print("end", head.next)
        return head.next