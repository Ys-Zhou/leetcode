# 25 / 25 test cases passed.
# Runtime: 36 ms


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        letters = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        length = len(digits)

        def getletter(index):
            if index == length:
                return ['']
            return [x + y for x in letters[digits[index]] for y in getletter(index + 1)]

        return getletter(0)
