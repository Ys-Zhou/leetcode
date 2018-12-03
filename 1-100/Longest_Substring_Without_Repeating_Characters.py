# 983 / 983 test cases passed.
# Runtime: 118 ms


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        record = dict()
        start_point = 0
        max_len = 0
        for i in xrange(len(s)):
            if record.has_key(s[i]):
                if record[s[i]] >= start_point:
                    start_point = record[s[i]] + 1
                record[s[i]] = i
            else:
                record.setdefault(s[i], i)
            max_len = max(max_len, i - start_point + 1)
        return max_len
