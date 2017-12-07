# 30 / 30 test cases passed.
# Runtime: 92 ms


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def getper(index):
            if index == len(nums):
                return [[]]
            res = []
            for prelist in getper(index + 1):
                for i in xrange(len(prelist) + 1):
                    if i != 0 and prelist[i - 1] == nums[index]:
                        break
                    res.append(prelist[0:i] + [nums[index]] + prelist[i:len(prelist)])
            return res

        return getper(0)
