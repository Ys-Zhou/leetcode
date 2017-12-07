# 169 / 169 test cases passed.
# Runtime: 92 ms

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x.start)
        res = []
        for i in xrange(1, len(intervals)):
            if intervals[i].start > intervals[i - 1].end:
                res.append(intervals[i - 1])
            else:
                intervals[i].start = intervals[i - 1].start
                intervals[i].end = max(intervals[i - 1].end, intervals[i].end)
        res.append(intervals[-1])
        return res
