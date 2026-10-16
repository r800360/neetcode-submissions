class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        max_money = [0] * n
        max_money[0] = nums[0]
        max_money[1] = max(nums[0], nums[1])
        for i in range(2, n):
            max_money[i] = max(nums[i] + max_money[i - 2], max_money[i-1])
        
        return max_money[n-1]