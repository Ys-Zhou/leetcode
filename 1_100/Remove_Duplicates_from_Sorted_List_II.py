# 168 / 168 test cases passed.
# Runtime: 59 ms

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nowval = None
        now = res = ListNode(None)
        while head:
            if head.val != nowval:
                if not head.next or head.val != head.next.val:
                    now.next = head
                    now = now.next
                else:
                    nowval = head.val
                    head = head.next
            head = head.next
        now.next = None
        return res.next
