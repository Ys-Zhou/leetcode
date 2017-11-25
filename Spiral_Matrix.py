#  22 / 22 test cases passed.
# Runtime: 32 ms


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        r, c = 0, 0
        while True:
            # right
            while c < n and matrix[r][c] is not None:
                res.append(matrix[r][c])
                matrix[r][c] = None
                c += 1
            r += 1
            c -= 1
            if r >= m or matrix[r][c] is None:
                break
            # down
            while r < m and matrix[r][c] is not None:
                res.append(matrix[r][c])
                matrix[r][c] = None
                r += 1
            r -= 1
            c -= 1
            if c < 0 or matrix[r][c] is None:
                break
            # left
            while c >= 0 and matrix[r][c] is not None:
                res.append(matrix[r][c])
                matrix[r][c] = None
                c -= 1
            r -= 1
            c += 1
            if r < 0 or matrix[r][c] is None:
                break
            # up
            while r >= 0 and matrix[r][c] is not None:
                res.append(matrix[r][c])
                matrix[r][c] = None
                r -= 1
            r += 1
            c += 1
            if c >= n or matrix[r][c] is None:
                break
        return res
