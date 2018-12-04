# Runtime: 164 ms, faster than 67.56% of Python online submissions


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        le = len(nums)
        if not nums or len(nums) < 4:
            return []
        sum_ab = dict()
        for a in xrange(0, le - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in xrange(a + 1, le - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                sum_k = nums[a] + nums[b]
                if sum_k in sum_ab:
                    sum_ab[sum_k].append([a, b])
                else:
                    sum_ab.setdefault(sum_k, [[a, b]])
        re = []
        for d in xrange(le - 1, 2, -1):
            if d < le - 1 and nums[d] == nums[d + 1]:
                continue
            for c in xrange(d - 1, 1, -1):
                if c < d - 1 and nums[c] == nums[c + 1]:
                    continue
                sum_k = target - (nums[c] + nums[d])
                if sum_k in sum_ab:
                    for idx_ab in sum_ab[sum_k]:
                        if idx_ab[1] < c:
                            re.append([nums[idx_ab[0]], nums[idx_ab[1]], nums[c], nums[d]])
        return re
