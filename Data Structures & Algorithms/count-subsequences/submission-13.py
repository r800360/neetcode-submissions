class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        if m < n:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # There is exactly one way to form an empty string
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(m):
            for j in range(n):
                # Don't use s[i]
                dp[i + 1][j + 1] = dp[i][j + 1]

                # Use s[i] if the characters match
                if s[i] == t[j]:
                    dp[i + 1][j + 1] += dp[i][j]

        return dp[m][n]