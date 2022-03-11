from math import inf


class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [0] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            res[i] = min(res[i + j] for j in range(1, min(nums[i] + 1, len(nums) - i))) + 1 if nums[i] > 0 else inf
        return res[0]
