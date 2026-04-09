class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) without using division
        # Approach: Use prefix sums
        product_left = [1]
        product_right = [1]
        n = len(nums)
        for i in range(1, n):
            product_left.append(product_left[-1] * nums[i-1])
            product_right.insert(0, product_right[0] * nums[n-i])
        
        return [x * y for x,y in zip(product_left, product_right)]

