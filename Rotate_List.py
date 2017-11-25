# 230 / 230 test cases passed.
# Runtime: 52 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        before = head
        after = head
        i = 1
        while i <= k:
            if before.next is None:
                k = i + k % i
                before = head
            else:
                before = before.next
            i += 1
        while before.next is not None:
            before = before.next
            after = after.next
        before.next = head
        head = after.next
        after.next = None
        return head
