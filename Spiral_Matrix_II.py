# 21 / 21 test cases passed.
# Runtime: 32 ms


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for x in xrange(n)]
        direction = 'right'
        row = 0
        col = -1
        num = 0
        changedir = {'right': 'down', 'down': 'left', 'left': 'up', 'up': 'right'}
        for i in xrange(2 * n - 2, -1, -1):
            for j in xrange(i / 2 + 1):
                num += 1
                if direction == 'right':
                    col += 1
                elif direction == 'down':
                    row += 1
                elif direction == 'left':
                    col -= 1
                elif direction == 'up':
                    row -= 1
                res[row][col] = num
            direction = changedir[direction]
        return res
