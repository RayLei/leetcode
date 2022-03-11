class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # dp = [[True] * len(nums)] * len(nums)
        dp = [[True, True, True], [True, True, True], [True, True, True]]

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + nums[i] + 1, len(nums), 1):
                if nums[i] >= 1:
                    dp[i][j] = any([dp[i][i + k] and dp[i + k][j] for k in range(1, nums[i]+1)])
                else:
                    dp[i][j] = False
        return dp[0][-1]


nums = [2,3,1,1,4]
a = Solution().canJump(nums)
print(a)



dp1 = [[True] * 3] * 3
dp2 = [[True, True, True], [True, True, True], [True, True, True]]

dp2[1][2] = False
dp1[1][2] = False

print(dp1)
print(dp2)
