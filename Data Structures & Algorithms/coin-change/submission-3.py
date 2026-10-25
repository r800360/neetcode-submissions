class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        num_coins = len(coins)
        intermediate = [0] * (amount + 1)
        for coin in coins:
            if coin < amount + 1:
                intermediate[coin] += 1
        for i in range(amount + 1):
            if intermediate[i]:
                for coin in coins:
                    if i + coin < amount + 1:
                        val = intermediate[i + coin]
                        if val:
                            intermediate[i + coin] = min(val, intermediate[i] + 1)
                        else:
                            intermediate[i + coin] = intermediate[i] + 1
        result = intermediate[-1]
        return result if result > 0 else -1