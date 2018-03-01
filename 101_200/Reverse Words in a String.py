# Python cannot do this problem in-place
# 22 / 22 test cases passed.
# Runtime: 29 ms


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = s.split()
        s_list.reverse()
        return ' '.join(s_list)
