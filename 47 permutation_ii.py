def permuteUnique(nums):

    def backtrack(nums):
        if len(nums) == 1:
            return [nums]

        res = []
        prv_val = -99
        for i in range(len(nums)):
            nums_tmp = nums.copy()
            n = nums_tmp.pop(i)
            if n == prv_val:
                continue
            res_tmp = backtrack(nums_tmp)
            for elem in res_tmp:
                elem.append(n)
            res.extend(res_tmp)
            prv_val = n

        return res

    result = backtrack(nums)
    return result


nums = [1, 1, 3]
t=permuteUnique(nums)
t
