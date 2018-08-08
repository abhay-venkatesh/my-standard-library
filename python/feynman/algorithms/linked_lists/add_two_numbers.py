class Solution:
    # by https://leetcode.com/tusizi
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(-1)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = v2.val
                v2 = v2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
