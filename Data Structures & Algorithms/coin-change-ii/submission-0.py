class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        intermediate = [0] * (amount + 1)
        intermediate[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                intermediate[i] += intermediate[i - coin]
        
        return intermediate[-1]