class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        # passby_idx = set()
        # dp = {}
        #
        # def dfs(i):
        #     if i in passby_idx:
        #         dp[i] = False
        #         return False
        #
        #     passby_idx.add(i)
        #     if arr[i] == 0:
        #         dp[i] = True
        #         return True
        #     if i in dp: return dp[i]
        #
        #     if i + arr[i] < len(arr) and i - arr[i] >= 0:
        #         res = dfs(i + arr[i]) or dfs(i - arr[i])
        #     elif i + arr[i] < len(arr):
        #         res = dfs(i + arr[i])
        #     elif i - arr[i] >= 0:
        #         res = dfs(i - arr[i])
        #     else:
        #         res= False
        #     dp[i] = res
        #     return res
        #
        # dfs(start)
        # return dp[start]

        passby_idx = set()

        def dfs(start):
            if start < 0 or start >= len(arr):
                return False
            if arr[start] == 0:
                return True
            if start in passby_idx:
                return False

            passby_idx.add(start)
            if self.canReach(arr, start + arr[start]):
                return True
            elif self.canReach(arr, start - arr[start]):
                return True
            return False

        return dfs(start)

arr = [3,0,2,1,2]
start = 2

a = Solution().canReach(arr, start)

