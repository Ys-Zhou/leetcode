# 8 / 8 test cases passed.
# Runtime: 43 ms


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def gen(left=n, right=n):
            if left == 0:
                return [')' * (right - left)]
            if left == right:
                return ['(' + y for y in gen(left - 1, right)]
            return ['(' + y for y in gen(left - 1, right)] + [')' + y for y in gen(left, right - 1)]

        return gen()
