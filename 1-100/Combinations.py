# Runtime: 124 ms, faster than 98.29% of Python online submissions
from itertools import combinations


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return [list(x) for x in combinations(xrange(1, n + 1), k)]
