class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for x in text1:
            prev_diag = 0

            for j, y in enumerate(text2, start=1):
                old = dp[j]

                if x == y:
                    dp[j] = prev_diag + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])

                prev_diag = old

        return dp[-1]