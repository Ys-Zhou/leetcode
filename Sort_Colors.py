# 86 / 86 test cases passed.
# Runtime: 35 ms


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pointer = [0] * 3
        for n in nums:
            for p in xrange(2, n - 1, -1):
                nums[pointer[p]] = p
                pointer[p] += 1
