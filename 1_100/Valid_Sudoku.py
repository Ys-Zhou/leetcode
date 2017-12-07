# 501 / 501 test cases passed.
# Runtime: 82 ms


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in xrange(3):
            for col in xrange(3):
                bit = 0
                for x in xrange(3):
                    for y in xrange(3):
                        if board[3 * row + x][3 * col + y] != '.':
                            nowbit = 1 << int(board[3 * row + x][3 * col + y]) - 1
                            if bit & nowbit:
                                return False
                            else:
                                bit |= nowbit
        for row in xrange(9):
            bit = 0
            for y in xrange(9):
                if board[row][y] != '.':
                    nowbit = 1 << int(board[row][y]) - 1
                    if bit & nowbit:
                        return False
                    else:
                        bit |= nowbit
        for col in xrange(9):
            bit = 0
            for x in xrange(9):
                if board[x][col] != '.':
                    nowbit = 1 << int(board[x][col]) - 1
                    if bit & nowbit:
                        return False
                    else:
                        bit |= nowbit
        return True
