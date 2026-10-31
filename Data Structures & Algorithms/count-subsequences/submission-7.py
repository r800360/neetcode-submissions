class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m < n:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for j in range(m):
            for i in range(n - 1, -1, -1):
                # Iterate from right to left to preserve the old value of dp[j] while updating dp[j + 1]
                # dp[i + 1][j + 1] = f(dp[i + 1][j], dp[i][j])
                if t[i] == s[j]:
                    dp[i + 1] += dp[i]

        return dp[-1]