# 61 / 61 test cases passed.
# Runtime: 55 ms


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])

        for x in xrange(row):
            for y in xrange(col):
                if x != 0:
                    if y != 0:
                        grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])
                    else:
                        grid[x][y] += grid[x - 1][y]
                else:
                    if y != 0:
                        grid[x][y] += grid[x][y - 1]
                    else:
                        pass
        return grid[row - 1][col - 1]
