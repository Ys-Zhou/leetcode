# 37 / 37 test cases passed.
# Runtime: 906 ms


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda (h, t): (-h, t))
        for i in xrange(len(people) - 1, -1, -1):
            for j in xrange(people[i][1]):
                people[i + j], people[i + j + 1] = people[i + j + 1], people[i + j]
        return people
