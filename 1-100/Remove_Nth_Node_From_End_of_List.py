# 207 / 207 test cases passed.
# Runtime: 45 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        before = after = head
        for i in xrange(n):
            before = before.next
        if not before:
            return head.next
        while before.next:
            before = before.next
            after = after.next
        after.next = after.next.next
        return head
