class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        # sum of all the elements in the array is even
        subset_sum = total // 2

        dp = [False] * (subset_sum + 1)
        dp[0] = True

        for num in nums:
            for i in range(subset_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[-1]
