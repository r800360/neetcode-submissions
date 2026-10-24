class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row, col = len(word1), len(word2)
        
        dp = [[0] * (col + 1) for _ in range(row + 1)]

        for r in range(row):
            dp[r][col] = row - r
        
        for c in range(col):
            dp[row][c] = col - c

        for r in reversed(range(row)):
            for c in reversed(range(col)):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = min(dp[r + 1][c], dp[r][c + 1], dp[r + 1][c + 1]) + 1
        
        return dp[0][0]