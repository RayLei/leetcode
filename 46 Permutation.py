from copy import copy

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def backtrack(nums):
        if len(nums) == 1: return [nums]

        tmp_res = backtrack(nums[:-1])
        res = []
        for elem in tmp_res:
            for j in range(len(elem) + 1):
                tmp_elem = copy(elem)
                tmp_elem.insert(j, nums[-1])
                res.append(tmp_elem)
        return res

    result = backtrack(nums)
    return result

nums = [1, 2]
permute(nums)

nums[::-1]
