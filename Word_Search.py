# 87 / 87 test cases passed.
# Runtime: 448 ms


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        len_word = len(word)

        def dfs(x, y, index):
            if index == len_word:
                return True
            if -1 < x < row and -1 < y < col and board[x][y] == word[index]:
                board[x][y] = None
                res = (dfs(x - 1, y, index + 1) or dfs(x + 1, y, index + 1) or
                       dfs(x, y - 1, index + 1) or dfs(x, y + 1, index + 1))
                board[x][y] = word[index]
                return res
            return False

        for ix in xrange(row):
            for iy in xrange(col):
                if dfs(ix, iy, 0):
                    return True
        return False
