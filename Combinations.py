# Correct but TLE


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def getcom(rest):
            if rest == 1:
                return [[x] for x in xrange(1, n + 1)]
            return [x + [y] for x in getcom(rest - 1) for y in xrange(x[-1] + 1, n + 1)]

        return getcom(k)
