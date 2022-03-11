def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    nums.sort()

    smallest_gap = 99999
    for i, x in enumerate(nums):
        old_gap = 99999
        l, r = i + 1, len(nums) - 1
        while l < r:
            new_gap = x + nums[l] + nums[r] - target
            if abs(new_gap) <= abs(old_gap):
                if new_gap > 0:
                    r -= 1
                elif new_gap < 0:
                    l += 1
                else:
                    return target

                old_gap = new_gap
            else:
                break
        if abs(old_gap) < abs(smallest_gap):
            smallest_gap = old_gap
    return smallest_gap + target


nums = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
target = 0

threeSumClosest(nums, target)


