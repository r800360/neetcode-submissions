class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        total_water = 0

        while left < right:
            # water[i] = max(0, min(L_max, R_max) - height[i])
            # we can calculate water just knowing one of L_max or R_max
            if height[left] <= height[right]:
                # Process left side
                total_water += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                # Process right side
                total_water += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1

        return total_water