# 25 / 25 test cases passed.
# Runtime: 65 ms

import itertools


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return map(list, itertools.permutations(nums))
