# 311 / 311 test cases passed.
# Runtime: 406 ms


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        res_li = [0] * (l1 + l2)

        for i in xrange(l1):
            for j in xrange(l2):
                index_1 = l1 - i - 1
                index_2 = l2 - j - 1
                pro = int(num1[index_1]) * int(num2[index_2])
                res_li[i + j] += pro

        carry = 0
        for p in xrange(l1 + l2):
            num = res_li[p]
            res_li[p] = (num + carry) % 10
            carry = (num + carry) / 10

        while len(res_li) > 1 and res_li[-1] == 0:
            res_li.pop()

        res = ''
        for q in xrange(len(res_li) - 1, -1, -1):
            res += str(res_li[q])
        return res
