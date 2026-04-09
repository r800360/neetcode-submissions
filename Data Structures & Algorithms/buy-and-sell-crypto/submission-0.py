class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        # prices is at least 2 elements
        # Dynamic sliding window
        left = 0
        max_profit = 0
        for right in range(1, n):
            curr_profit = prices[right] - prices[left]
            max_profit = max(max_profit, curr_profit)
            while (prices[left] > prices[right]):
                left += 1

        return max_profit
