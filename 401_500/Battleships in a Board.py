class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board:
            return 0
        count = 0
        for x in xrange(len(board)):
            for y in xrange(len(board[0])):
                if board[x][y] == 'X' and (x == 0 or board[x - 1][y] == '.') and (y == 0 or board[x][y - 1] == '.'):
                    count += 1
        return count
