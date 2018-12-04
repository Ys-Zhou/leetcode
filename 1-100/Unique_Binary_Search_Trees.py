# Runtime: 20 ms, faster than 94.24% of Python online submissions


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        dp = [0 for _ in xrange(n + 1)]
        dp[0] = dp[1] = 1
        for x in xrange(2, n + 1):
            for left in xrange(0, x):
                dp[x] += dp[left] * dp[x - left - 1]
        return dp[n]
