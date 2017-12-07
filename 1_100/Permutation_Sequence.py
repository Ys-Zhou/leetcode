# 200 / 200 test cases passed.
# Runtime: 32 ms

import math


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        layer = math.factorial(n - 1)
        cands = range(1, n + 1)
        res = ''
        k -= 1
        for i in xrange(n - 1, 0, -1):
            index = k / layer
            res += str(cands[index])
            cands.pop(index)
            k %= layer
            layer /= i
        res += str(cands[0])
        return res
