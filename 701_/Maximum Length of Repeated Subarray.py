# 54 / 54 test cases passed.
# Runtime: 3304 ms


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        rec = [[0] * len(B) for _ in A]
        for i in xrange(len(A)):
            for j in xrange(len(B)):
                if A[i] == B[j]:
                    if i != 0 and j != 0:
                        rec[i][j] = rec[i - 1][j - 1] + 1
                    else:
                        rec[i][j] = 1
        return max([max(x) for x in rec])
