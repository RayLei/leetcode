def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    l, r = 0, len(nums) - 1
    res = -1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] > max(nums[l], nums[r]):  # m in 1st half and rotated
            if nums[l] < target < nums[m]:
                r = m - 1  # t in 1st
            elif target > nums[m] or target < nums[l]:
                l = m + 1  # t in 2nd or 3rd
            elif target == nums[l]:
                return l
        elif nums[m] < min(nums[l], nums[r]):  # m in 2nd half and rotated
            if nums[m] < target < nums[r]:
                l = m + 1  # t in 3rd
            elif target < nums[m] or target > nums[r]:
                r = m - 1  # t in 1st and 2nd
            elif target == nums[r]:
                return r
        elif nums[l] < nums[m] < nums[r]:   # non-rotated
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
        elif nums[m] == nums[l]:           # len 2
            if target == nums[r]:
                return r
            else:
                return res
    return res



nums = [3, 1]
t = 0

print(search(nums, t))
