class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        h1, h2, h3 = l1, l2, l3
        carry = 0
        while h1 or h2 or carry:
            val1 = h1.val if h1 else 0
            val2 = h2.val if h2 else 0

            cursum = val1 + val2 + carry
            h3.next = ListNode(cursum % 10)
            carry = cursum // 10
            h1 = h1.next if h1 else None
            h2 = h2.next if h2 else None
            h3 = h3.next

        return l3.next