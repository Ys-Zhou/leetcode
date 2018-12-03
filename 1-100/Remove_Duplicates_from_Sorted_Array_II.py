# 164 / 164 test cases passed.
# Runtime: 66 ms


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = len(nums)
        if total <= 2:
            return total
        forward = 0
        for i in xrange(2, total):
            if nums[i] == nums[i - forward - 1] == nums[i - forward - 2]:
                forward += 1
            else:
                nums[i - forward] = nums[i]
        return total - forward
