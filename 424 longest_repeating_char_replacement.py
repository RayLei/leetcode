class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        count = {}
        max_len = 0

        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)

            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1       # reduce the count at the left
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len

s = "AABABBA"; k = 1
print(Solution().characterReplacement(s, k))


