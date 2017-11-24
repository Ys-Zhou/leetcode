# 94 / 94 test cases passed.
# Runtime: 2315 ms


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 1
        output = s[0]
        for i in xrange(len(s)):
            j = 1
            while i - j > -1 and i + j < len(s):
                if s[i - j] == s[i + j]:
                    if 2 * j + 1 > max_len:
                        max_len = 2 * j + 1
                        output = s[i - j:i + j + 1]
                    j += 1
                else:
                    break
        for i in xrange(len(s) - 1):
            j = 0
            while i - j > -1 and i + j + 1 < len(s):
                if s[i - j] == s[i + j + 1]:
                    if 2 * j + 2 > max_len:
                        max_len = 2 * j + 2
                        output = s[i - j:i + j + 2]
                    j += 1
                else:
                    break
        return output
