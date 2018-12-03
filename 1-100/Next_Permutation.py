# 265 / 265 test cases passed.
# Runtime: 62 ms


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = len(nums)
        if count < 2:
            return
        i = count - 2
        while i > -1 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            nums.reverse()
            return
        j = i + 1
        while j < count and nums[j] > nums[i]:
            j += 1
        nums[i], nums[j - 1] = nums[j - 1], nums[i]
        left, right = i + 1, count - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
