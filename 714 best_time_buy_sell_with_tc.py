from math import inf

class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        tc = fee / 2
        rest, hold = 0, -inf
        for p in prices:
            prv_rest = rest
            rest = max(rest, hold + p - tc)
            hold = max(hold, prv_rest - p - tc)
        return int(rest)

prices = [1,3,2,8,4,9]
fee = 2

a = Solution().maxProfit(prices, fee)
print(a)
