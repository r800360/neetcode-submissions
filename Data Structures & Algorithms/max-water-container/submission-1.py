class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0
        while (left < right):
            if heights[left] <= heights[right]:
                currArea = (right - left) * heights[left]
                maxArea = max(maxArea, currArea)
                left += 1
            else:
                currArea = (right - left) * heights[right]
                maxArea = max(maxArea, currArea)
                right -= 1
            

        return maxArea