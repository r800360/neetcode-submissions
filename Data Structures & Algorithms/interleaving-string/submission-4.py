class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        # Keep the DP array as small as possible.
        if n > m:
            s1, s2 = s2, s1
            m, n = n, m

        # dp[j] represents whether the current prefix of s1 and s2[:j] can form the corresponding s3 prefix.
        dp = [False] * (n + 1)
        dp[0] = True

        # Initialize the first row.
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        # Process subsequent rows.
        for i in range(1, m + 1):
            # Update the first column.
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                curr_char = s3[i + j - 1]

                # dp[j] is still the value from the previous row.
                # dp[j-1] is already updated for the current row.
                dp[j] = ((dp[j] and s1[i - 1] == curr_char) or (dp[j - 1] and s2[j - 1] == curr_char))

        return dp[n]