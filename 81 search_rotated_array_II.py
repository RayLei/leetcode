def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """

    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2

        if target == nums[m]:
            return True
        elif nums[l] == nums[m] == nums[r] and l != r:
            for i in range(1, m+1):
                if nums[m - i] != nums[m]:  # right is constant
                    r = m - i
                    break
                if nums[m + i] != nums[m]:  # left is constant
                    l = m + i
                    break
                if i == m:      # array is constant
                    return False
        elif nums[l] <= nums[m]:
            if nums[l] < target < nums[m]:
                r = m - 1
            elif target < nums[l] or target > nums[m]:
                l = m + 1
            else:
                return True
        elif nums[m] <= nums[r]:
            if nums[m] < target < nums[r]:
                l = m + 1
            elif target < nums[m] or target > nums[r]:
                r = m - 1
            else:
                return True
    return False


nums = [1,1,1,1,3,1]
target = 3

search(nums, target)
