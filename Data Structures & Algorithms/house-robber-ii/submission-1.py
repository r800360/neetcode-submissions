class Solution:
    def rob(self, nums: List[int]) -> int:
        # solve the original house robber twice - from 0 to n - 2 (exclude last house) and 1 to n - 1 (exclude first house)
        def rob_linear(houses):
            prev2, prev1 = 0, 0

            for num in houses:
                curr = max(num + prev2, prev1)
                prev2, prev1 = prev1, curr

            return prev1

        if len(nums) == 1:
            return nums[0]

        return max(
            rob_linear(nums[:-1]),  # Exclude last house
            rob_linear(nums[1:])    # Exclude first house
        )