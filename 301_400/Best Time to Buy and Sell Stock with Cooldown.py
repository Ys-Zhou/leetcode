# 211 / 211 test cases passed.
# Runtime: 40 ms
import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        last_standby, standby = None, 0
        last_holding, holding = None, -sys.maxint - 1
        last_cooling, cooling = None, -sys.maxint - 1

        for price in prices:
            last_standby = standby
            last_holding = holding
            last_cooling = cooling

            standby = max(last_standby, last_cooling)
            holding = max(last_standby - price, last_holding)
            cooling = last_holding + price

        return max(standby, cooling)
