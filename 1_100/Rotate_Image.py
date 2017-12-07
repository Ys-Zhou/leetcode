# 21 / 21 test cases passed.
# Runtime: 36 ms


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for x in xrange(1, n):
            for y in xrange(x):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        for x in xrange(n):
            for y in range(n / 2):
                matrix[x][y], matrix[x][n - 1 - y] = matrix[x][n - 1 - y], matrix[x][y]
