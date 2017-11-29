# Incomprehensible TLE


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0

        def count(index):
            if index == length:
                return 1
            if s[index] == '0':
                return 0
            if index == length - 1:
                return 1
            if int(s[index:index + 2]) <= 26:
                return count(index + 1) + count(index + 2)
            return count(index + 1)

        return count(0)
