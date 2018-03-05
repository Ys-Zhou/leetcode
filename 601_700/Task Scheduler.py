# 64 / 64 test cases passed.
# Runtime: 299 ms
import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = collections.Counter(tasks)
        maxtask = max(c.values())
        last = c.values().count(maxtask)
        return max(len(tasks), (maxtask - 1) * (n + 1) + last)
