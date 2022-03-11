def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    def binarySearch(l, r, left_bias):
        res = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                res = m
                if left_bias:
                    r = m - 1
                else:
                    l = m + 1
        return res

    l_p = binarySearch(0, len(nums) - 1, True)
    r_p = binarySearch(0, len(nums) - 1, False)
    return [l_p, r_p]


nums = [5,7,7,8,8,10]
t = searchRange(nums, 6)
print(t)
