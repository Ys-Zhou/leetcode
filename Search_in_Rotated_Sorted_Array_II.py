# 273 / 273 test cases passed.
# Runtime: 35 ms


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        first = 0
        last = len(nums) - 1
        while first < last and nums[first] == nums[last]:
            last -= 1
        while first <= last:
            p = (first + last) / 2
            if nums[p] == target:
                return True
            if nums[0] <= nums[first] <= nums[last] or nums[first] <= nums[last] < nums[0]:
                if nums[p] < target:
                    first = p + 1
                else:
                    last = p - 1
            else:
                if nums[p] < target < nums[0] or target < nums[0] <= nums[p] or nums[0] <= nums[p] < target:
                    first = p + 1
                else:
                    last = p - 1
        return False
