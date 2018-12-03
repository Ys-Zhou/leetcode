# 147 / 147 test cases passed.
# Runtime: 49 ms


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        length = len(s)
        if length < 4:
            return res
        for a in xrange(1, 4):
            if length - a < 3 or length - a > 9 or int(s[0:a]) > 255 or (s[0] == '0' and a > 1):
                continue
            for b in xrange(1, 4):
                if length - a - b < 2 or length - a - b > 6 or int(s[a:a + b]) > 255 or (s[a] == '0' and b > 1):
                    continue
                for c in xrange(1, 4):
                    if length - a - b - c < 1 or length - a - b - c > 3 or int(s[a + b:a + b + c]) > 255 or (
                            s[a + b] == '0' and c > 1):
                        continue
                    if int(s[a + b + c:length]) > 255 or (s[a + b + c] == '0' and length - a - b - c > 1):
                        continue
                    res.append('%s.%s.%s.%s' % (s[0:a], s[a:a + b], s[a + b:a + b + c], s[a + b + c:length]))
        return res
