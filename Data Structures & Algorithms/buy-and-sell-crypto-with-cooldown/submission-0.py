class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # Base cases for Day 1
        hold, sold, rest = -prices[0], 0, 0

        for i in range(n):
            prev_sold = sold
            sold = hold + prices[i]
            hold = max(hold, rest - prices[i])
            rest = max(rest, prev_sold)

        # On the final day, either sold or rest (cannot hold)
        return max(sold, rest)