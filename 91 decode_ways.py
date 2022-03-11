class Solution:
    def numDecodings(self, s: str) -> int:
        nums = [str(i) for i in range(1, 27)]

        def dfs(i):
            if i >= len(s):
                return 1

            if s[i] in nums and i + 2 <= len(s) and s[i:i + 2] in nums:
                res = dfs(i + 1) + dfs(i + 2)
            elif s[i] in nums:
                res = dfs(i + 1)
            else:
                res = 0

            return res

        result = dfs(0)
        return result


s = '06'
a = Solution().numDecodings(s)
print(a)
