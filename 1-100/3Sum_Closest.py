# 125 / 125 test cases passed.
# Runtime: 159 ms


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        closest = float('inf')
        for i in xrange(length):
            if 3 * nums[i] > target + abs(closest):
                break
            x = i + 1
            y = length - 1
            while x < y:
                sum_ = nums[i] + nums[x] + nums[y]
                if sum_ == target:
                    return target
                if abs(sum_ - target) < abs(closest - target):
                    closest = sum_
                if sum_ < target:
                    x += 1
                else:
                    y -= 1
        return closest
