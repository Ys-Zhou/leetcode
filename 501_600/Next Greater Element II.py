# 224 / 224 test cases passed.
# Runtime: 349 ms


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [-1] * length
        stack = []
        for i in xrange(length):
            while stack and stack[-1][0] < nums[i]:
                res[stack[-1][1]] = nums[i]
                stack.pop()
            stack.append((nums[i], i))
        for i in xrange(length):
            if not stack or stack[-1][1] == i:
                break
            while stack and stack[-1][0] < nums[i]:
                res[stack[-1][1]] = nums[i]
                stack.pop()
        return res
