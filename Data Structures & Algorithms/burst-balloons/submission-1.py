class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # pad with ones on each side
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        # dp[l][r] := maxCoins bursting every balloon in [l, r], assuming the balloons outside that interval remain
        # dp[l][r] = dp[l][i-1] + max_{l <= i <= r} nums[l-1] * nums[i] * nums[r + 1] + dp[i+1][r] essentially
        for length in range(1, n+1):
            for l in range(n - length + 1):
                r = l + length - 1
                dp[l][r] = -1
                for i in range(l, r + 1):
                    # Calculate dp[l][r]
                    dp[l][r] = max(dp[l][r], dp[l][i - 1] + nums[l - 1] * nums[i] * nums[r + 1] + dp[i + 1][r])
        return dp[0][n-1]