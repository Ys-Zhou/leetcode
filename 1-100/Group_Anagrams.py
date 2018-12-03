# 101 / 101 test cases passed.
# Runtime: 228 ms
import string


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                     101]
        primes = dict(zip(string.ascii_lowercase, primeList))

        resDict = dict()
        for s in strs:
            spe = 1
            for c in s:
                spe *= primes[c]
            if spe in resDict:
                resDict[spe].append(s)
            else:
                resDict.setdefault(spe, [s])
        return resDict.values()
