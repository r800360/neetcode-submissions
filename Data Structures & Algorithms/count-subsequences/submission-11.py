class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m < n:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(m):
            for j in range(n - 1, -1, -1):
                # Iterate from right to left to preserve the old value of dp[j] while updating dp[j + 1]
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]

        return dp[-1]