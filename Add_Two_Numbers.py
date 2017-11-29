# 1562 / 1562 test cases passed.
# Runtime: 136 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        node = head = ListNode(None)
        while l1 and l2:
            sum_ = l1.val + l2.val + carry
            node.next = ListNode(sum_ % 10)
            carry = sum_ / 10
            l1, l2, node = l1.next, l2.next, node.next
        while l1:
            sum_ = l1.val + carry
            node.next = ListNode(sum_ % 10)
            carry = sum_ / 10
            l1, node = l1.next, node.next
        while l2:
            sum_ = l2.val + carry
            node.next = ListNode(sum_ % 10)
            carry = sum_ / 10
            l2, node = l2.next, node.next
        if carry != 0:
            node.next = ListNode(carry)
        return head.next
