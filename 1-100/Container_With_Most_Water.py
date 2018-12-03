# 49 / 49 test cases passed.
# Runtime: 78 ms


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxwater = 0
        while left < right:
            maxwater = max(maxwater, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxwater
