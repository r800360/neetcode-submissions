class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] is the length of the LIS ending at exactly index i
        # dp[i] = 1 + max_{j < i a_j < a_i} dp[j]
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            dp_max = -1
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    dp_max = max(dp_max, dp[j])
            if dp_max == -1:
                dp[i] = 1
            else:
                dp[i] = 1 + dp_max
        
        return max(dp)