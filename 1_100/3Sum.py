# 313 / 313 test cases passed.
# Runtime: 1355 ms


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s_nums = sorted(nums)
        l_list = len(s_nums)
        output = []
        for i in xrange(0, l_list - 2):
            if i != 0:
                if s_nums[i - 1] == s_nums[i]:
                    continue
            x = i + 1
            y = l_list - 1
            while x < y:
                sum_ = s_nums[i] + s_nums[x] + s_nums[y]
                if sum_ == 0:
                    if not output:
                        output.append([s_nums[i], s_nums[x], s_nums[y]])
                    elif not (output[-1][1] == s_nums[x] and output[-1][2] == s_nums[y]):
                        output.append([s_nums[i], s_nums[x], s_nums[y]])
                    x += 1
                    y -= 1
                elif sum_ < 0:
                    x += 1
                else:
                    y -= 1
        return output
