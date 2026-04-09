class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # result = nums[0]
        # for i in range(1, len(nums)):
        #     result = result ^ nums[i]
        # return result
        result = 0
        for num in nums:
            result ^= num
        return result