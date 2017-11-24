# 87 / 87 test cases passed.
# Runtime: 35 ms


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        first = 0
        last = len(nums) - 1
        p = last / 2
        while first <= last:
            if nums[p] < target:
                first = p + 1
            elif nums[p] > target:
                last = p - 1
            else:
                break
            p = (first + last) / 2
        else:
            return [-1, -1]
        return [self.searchforStart(nums, target, first, last), self.searchforEnd(nums, target, first, last)]

    def searchforStart(self, nums, target, first, last):
        p = (first + last) / 2
        while not (nums[p] == target and (p == 0 or nums[p] != nums[p - 1])):
            if nums[p] < target:
                first = p + 1
            else:
                last = p - 1
            p = (first + last) / 2
        return p

    def searchforEnd(self, nums, target, first, last):
        last_i = len(nums) - 1
        p = (first + last) / 2
        while not (nums[p] == target and (p == last_i or nums[p] != nums[p + 1])):
            if nums[p] <= target:
                first = p + 1
            else:
                last = p - 1
            p = (first + last) / 2
        return p
