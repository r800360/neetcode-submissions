class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # O(n^2) time and O(1) space
        n = len(heights)
        max_area = 0
        width = 0
        for i in range(n):
            index = i
            current_height = heights[i]
            width = 1
            while index - 1 >= 0 and heights[index - 1] >= current_height:
                width += 1
                index -= 1
            index = i
            while index + 1 < n and heights[index + 1] >= current_height:
                width += 1
                index += 1
            max_area = max(max_area, width*current_height)
        return max_area