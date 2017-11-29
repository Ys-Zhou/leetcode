# 10 / 10 test cases passed.
# Runtime: 65 ms


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            for index in xrange(len(res)):
                res.append(res[index] + [i])
        return res
