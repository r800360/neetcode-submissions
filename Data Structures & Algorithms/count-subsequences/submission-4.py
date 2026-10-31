class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m = len(s)
        n = len(t)
        if m < n:
            return 0
        # dp[i][j] = number of ways to form t[:i+1] using characters from s[:j+1]
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        # if t is empty or i = 0 there is always 1 way to construct it
        for j in range(m + 1):
            dp[0][j] = 1

        for i in range(n):
            for j in range(i, m):
                if t[i] == s[j]:
                    # We can either use s[j] or not use s[j]
                    # number of ways to construct the same prefix of t
                    dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j]
                else:
                    # Accumulate from the left
                    dp[i + 1][j + 1] = dp[i + 1][j]

        return dp[-1][-1]