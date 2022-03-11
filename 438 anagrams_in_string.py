class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        res = []
        l = r = 0

        # get length and count of string p
        len_p = len(p)
        cnt_p = {}
        for x in p:
            cnt_p[x] = 1 + cnt_p.get(x, 0)

        # get count for a window in s
        cnt_s = {}
        while r < len(s):
            if s[r] not in cnt_p.keys():
                l = r + 1
                cnt_s = {}
            else:
                cnt_s[s[r]] = 1 + cnt_s.get(s[r], 0)   # update the count in the window

                if r - l + 1 == len_p:
                    if cnt_p == cnt_s:
                        res.append(l)
                    cnt_s[s[l]] -= 1     # slide the window
                    l += 1

            r += 1
        return res


s="abab"
p="ab"

print(Solution().findAnagrams(s,p))
