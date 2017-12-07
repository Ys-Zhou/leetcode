# 166 / 166 test cases passed.
# Runtime: 42 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        pre = prehead = ListNode(None)
        lat = lathead = ListNode(None)
        while head:
            if head.val < x:
                pre.next = head
                pre = pre.next
            else:
                lat.next = head
                lat = lat.next
            head = head.next
        lat.next = None
        pre.next = lathead.next
        return prehead.next
