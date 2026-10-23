class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(start, end):
            prev2, prev1 = 0, 0

            for i in range(start, end):
                curr = max(prev1, prev2 + nums[i])
                prev2, prev1 = prev1, curr

            return prev1

        n = len(nums)

        if n == 1:
            return nums[0]

        return max(
            rob_range(0, n - 1),  # Exclude last house
            rob_range(1, n)        # Exclude first house
        )