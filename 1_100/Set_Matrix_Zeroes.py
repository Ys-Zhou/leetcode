# 157 / 157 test cases passed.
# Runtime: 209 ms


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])

        def markZero(ix, iy):
            for j in xrange(col):
                if matrix[ix][j] != 0:
                    matrix[ix][j] = None
            for i in xrange(row):
                if matrix[i][iy] != 0:
                    matrix[i][iy] = None

        for x in xrange(row):
            for y in xrange(col):
                if matrix[x][y] == 0:
                    markZero(x, y)
        for x in xrange(row):
            for y in xrange(col):
                if matrix[x][y] is None:
                    matrix[x][y] = 0
