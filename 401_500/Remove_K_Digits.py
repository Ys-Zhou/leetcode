# 33 / 33 test cases passed.
# Runtime: 72 ms


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = []
        for c in num:
            while k > 0 and res and int(res[-1]) > int(c):
                res.pop()
                k -= 1
            res.append(c)
        if k != 0:
            res = res[0:-k]
        if not res:
            return '0'
        return str(int(''.join(res)))
