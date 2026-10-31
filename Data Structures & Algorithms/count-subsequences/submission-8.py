class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        if m < n:
            return 0

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # There is exactly one way to form an empty string
        for j in range(m + 1):
            dp[j][0] = 1

        for j in range(m):
            for i in range(n):
                # Don't use s[j]
                dp[j + 1][i + 1] = dp[j][i + 1]

                # Use s[j] if the characters match
                if s[j] == t[i]:
                    dp[j + 1][i + 1] += dp[j][i]

        return dp[m][n]