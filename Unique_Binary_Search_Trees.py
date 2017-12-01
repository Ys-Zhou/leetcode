# Correct but TLE


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1
        return reduce(lambda x, y: x + y, [self.numTrees(i) * self.numTrees(n - 1 - i) for i in xrange(n)])


s = Solution()
print s.numTrees(9)
