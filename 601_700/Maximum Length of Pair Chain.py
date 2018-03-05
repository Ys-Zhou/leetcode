# 202 / 202 test cases passed.
# Runtime: 83 ms


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        num = 0
        last = -9223372036854775808
        pairs.sort(key=lambda x: x[1])
        for pair in pairs:
            if pair[0] > last:
                num += 1
                last = pair[1]
        return num
