# 43 / 43 test cases passed.
# Runtime: 42 ms


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        for x in xrange(row):
            for y in xrange(col):
                if obstacleGrid[x][y] == 1:
                    obstacleGrid[x][y] = 0
                    continue
                if x != 0:
                    if y != 0:
                        obstacleGrid[x][y] = obstacleGrid[x - 1][y] + obstacleGrid[x][y - 1]
                    else:
                        obstacleGrid[x][y] = obstacleGrid[x - 1][y]
                else:
                    if y != 0:
                        obstacleGrid[x][y] = obstacleGrid[x][y - 1]
                    else:
                        obstacleGrid[x][y] = 1
        return obstacleGrid[row - 1][col - 1]
