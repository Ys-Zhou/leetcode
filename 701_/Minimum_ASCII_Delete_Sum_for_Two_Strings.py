# 93 / 93 test cases passed.
# Runtime: 1080 ms


class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        p = [[0] * (len(s2) + 1) for _ in xrange(len(s1) + 1)]
        for x in xrange(len(s1)):
            p[x + 1][0] = p[x][0] + ord(s1[x])
        for y in xrange(len(s2)):
            p[0][y + 1] = p[0][y] + ord(s2[y])
        for x in xrange(len(s1)):
            for y in xrange(len(s2)):
                if s1[x] == s2[y]:
                    p[x + 1][y + 1] = p[x][y]
                else:
                    p[x + 1][y + 1] = min(p[x + 1][y] + ord(s2[y]), p[x][y + 1] + ord(s1[x]))
        return p[len(s1)][len(s2)]
