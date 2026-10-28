class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        total = sum(nums)
        if target > total or target < -total:
            return 0
        
        # Idea: convert this into a subset sums problem!
        # P - N = target
        # P + N = sum(nums)
        # P = (target + sum(nums))/2
        if (target + total) % 2 == 1:
            return 0

        subset_target = (target + total) // 2
        dp = [0] * (subset_target + 1)
        dp[0] = 1
        for num in nums:
            for s in range(subset_target, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[subset_target]