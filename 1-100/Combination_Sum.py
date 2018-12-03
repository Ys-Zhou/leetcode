# 168 / 168 test cases passed.
# Runtime: 375 ms
import copy


class Solution(object):
    def __init__(self):
        self.result = []
        self.sortedCand = []
        self.length = None

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.sortedCand = sorted(candidates)
        self.length = len(candidates)
        self.searchPath(0, target, [])
        return self.result

    def searchPath(self, nowIndex, target, path):
        if nowIndex < self.length:
            if target == 0:
                self.result.append(path)
            elif target > 0:
                # Choose nowIndex
                pathC = copy.copy(path)
                pathC.append(self.sortedCand[nowIndex])
                self.searchPath(nowIndex, target - self.sortedCand[nowIndex], pathC)
                # Not choose nowIndex
                self.searchPath(nowIndex + 1, target, path)
        return
