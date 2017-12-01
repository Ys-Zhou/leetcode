# 44 / 44 test cases passed.
# Runtime: 33 ms


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        newhead = ListNode(0)
        newhead.next = head
        first = newhead
        for i in xrange(m - 1):
            first = first.next
        p = first.next
        q = p.next
        for i in xrange(n - m):
            temp = q.next
            q.next = p
            p, q = q, temp
        first.next.next = q
        first.next = p
        return newhead.next
