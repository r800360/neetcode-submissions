class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best_product = nums[0]
        current_product = 1

        for num in nums:
            current_product *= num
            best_product = max(best_product, current_product)

            if num == 0:
                current_product = 1

        current_product = 1

        for num in reversed(nums):
            current_product *= num
            best_product = max(best_product, current_product)

            if num == 0:
                current_product = 1

        return best_product