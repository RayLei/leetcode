class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        max_len = 0

        while r < len(s):
            while l < r and s[r] in s[l:r]:
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len


s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
