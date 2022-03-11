class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals = sorted(intervals, key=lambda x: x[0], reverse=False)

        res = []
        left, right = intervals[0]
        for i, (l , r) in enumerate(intervals[1:]):
            if r <= right:        # included
                continue
            elif l <= right:      # continuous included
                right = r
            else:                 # break, e.g. l > right
                res.append([left, right].copy())
                left, right = l , r
        res.append([left, right])
        return res


intervals = [[1,4],[4,5]]
print(Solution().merge(intervals))
