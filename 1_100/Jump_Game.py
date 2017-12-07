# 75 / 75 test cases passed.
# Runtime: 75 ms


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farIndex = 0
        length = len(nums)
        for i in xrange(length):
            if i <= farIndex:
                farIndex = max(farIndex, i + nums[i])
            if farIndex >= length - 1:
                return True
        return False
