# 136 / 136 test cases passed.
# Runtime: 36 ms


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        if not row:
            return False
        col = len(matrix[0])
        if not col:
            return False

        small = 0
        large = row - 1
        while small < large:
            mid = (small + large) / 2 + 1
            if matrix[mid][0] > target:
                large = mid - 1
            elif matrix[mid][0] < target:
                small = mid
            else:
                return True

        before = 0
        after = col - 1
        while before <= after:
            index = (before + after) / 2
            if matrix[small][index] > target:
                after = index - 1
            elif matrix[small][index] < target:
                before = index + 1
            else:
                return True

        return False
