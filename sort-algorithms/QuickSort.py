def quick_sort(nums):
    if not nums:
        return
    sort_(0, len(nums) - 1, nums)


def sort_(start, end, nums):
    if end - start <= 0:
        return
    left = start
    right = end
    while left < right:
        if nums[left] < nums[end]:
            left += 1
            continue
        if nums[right] >= nums[end]:
            right -= 1
            continue
        nums[left], nums[right] = nums[right], nums[left]
    nums[right], nums[end] = nums[end], nums[right]
    sort_(start, right - 1, nums)
    sort_(right + 1, end, nums)


n = [3, 7, 2, 4, 1, 5, 1, 3, 7, 4, 1, 4, 6]
quick_sort(n)
print n
