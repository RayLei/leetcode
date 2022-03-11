from math import inf
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        rest, hold, sold = 0, -inf, 0
        for i in range(len(prices)):
            prev_hold = hold
            hold = max(hold, rest - prices[i])
            rest = max(rest, sold)
            sold = prev_hold + prices[i]

        return max(sold, rest)

