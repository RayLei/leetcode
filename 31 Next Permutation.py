class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        r = len(nums) - 1
        while r > 0 and nums[r] <= nums[r - 1]:
            r -= 1

        if r == 0:  # if not found
            return nums[::-1]
        else:  # if found
            p = v = r
            # find the smallest value larger than nums[r-1]
            while p < len(nums):
                if nums[p] > nums[r - 1] and nums[p] < nums[v]:
                    v = p
                p += 1

            tmp = nums[v]
            nums[v] = nums[r - 1]
            nums[r - 1] = tmp
            nums[r:] = sorted(nums[r:])
            return nums


nums = [1, 2, 3]
nums2 = [3, 2, 1]
test = Solution()
print(test.nextPermutation(nums))
print(test.nextPermutation(nums2))

