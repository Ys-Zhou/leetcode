def merge(list1, list2):
    res = []
    len1, len2 = len(list1), len(list2)
    i1, i2 = 0, 0
    while i1 < len1 and i2 < len2:
        if list1[i1] < list2[i2]:
            res.append(list1[i1])
            i1 += 1
        else:
            res.append(list2[i2])
            i2 += 1
    if i1 < len1:
        return res + list1[i1:len1]
    if i2 < len2:
        return res + list2[i2:len2]


def merge_sort(nums):
    list_ = [[x] for x in nums]
    while len(list_) > 1:
        list_n = []
        for i in xrange(len(list_) / 2):
            list_n.append(merge(list_[2 * i], list_[2 * i + 1]))
        if len(list_) % 2:
            list_n.append(list_[-1])
        list_ = list_n
    return list_[0]


n = [3, 7, 2, 4, 1, 5, 1, 3, 7, 4, 1, 4, 6]
print merge_sort(n)
