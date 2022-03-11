class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        actual_sum, max_len = 0, 0

        while r < len(nums):
            actual_sum += nums[r]
            target_sum = nums[r] * (r - l + 1)
            if target_sum - actual_sum <= k:
                max_len = max(max_len, r - l + 1)
            else:
                actual_sum -= nums[l]
                l += 1
            r += 1
        return max_len


nums = [3, 9, 6]; k = 2
a = Solution().maxFrequency(nums, k)
print(a)


