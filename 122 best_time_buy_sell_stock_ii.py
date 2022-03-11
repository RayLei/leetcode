class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        all_profit, profit = 0, 0
        l, r = 0, 1

        while r < len(prices):
            if prices[r] > max(prices[l], prices[r - 1]):
                profit = prices[r] - prices[l]
            else:
                l = r
                all_profit += profit
                profit = 0

            if r == len(prices) - 1 and prices[r] > max(prices[l], prices[r - 1]):
                all_profit += profit

            r += 1

        return all_profit


prices = [3,2,6,5,0,3]
a = Solution().maxProfit(prices)
print(a)
