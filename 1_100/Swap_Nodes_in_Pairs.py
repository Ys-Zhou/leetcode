# 55 / 55 test cases passed.
# Runtime: 36 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            if head.next:
                next_ = head.next.next
                pre = head.next
                pre.next = head
                pre.next.next = self.swapPairs(next_)
                return pre
            else:
                return head
        else:
            return None
