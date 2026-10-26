class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2
        bits = 1

        for num in nums:
            bits |= bits << num

        return bool((bits >> target) & 1)