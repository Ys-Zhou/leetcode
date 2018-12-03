# 172 / 172 test cases passed.
# Runtime: 175 ms


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        total = len(candidates)
        res = []

        def cal(list_, sum_, index, avoid):
            if sum_ == target:
                res.append(list_)
                return
            if sum_ > target:
                return
            if index == total:
                return
            if candidates[index] != avoid:
                cal(list_ + [candidates[index]], sum_ + candidates[index], index + 1, None)
            cal(list_, sum_, index + 1, candidates[index])

        cal([], 0, 0, None)
        return res
