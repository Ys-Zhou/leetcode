# 19 / 19 test cases passed.
# Runtime: 59 ms


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        val = None
        length = 0
        if not nums:
            return res
        nums.sort()
        for n in nums:
            if n == val:
                nowlength = len(res)
                for index in xrange(nowlength - length, nowlength):
                    res.append(res[index] + [n])
            else:
                val = n
                length = len(res)
                for index in xrange(length):
                    res.append(res[index] + [n])
        return res
