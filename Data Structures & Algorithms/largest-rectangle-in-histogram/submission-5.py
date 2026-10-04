class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # O(n) time and O(1) space
        n = len(heights)
        base = n + 1
        top = -1
        max_area = 0

        for i, height in enumerate(heights + [0]):
            while top != -1:
                encoded = heights[top]
                curr_height = encoded // base
                prev = encoded % base - 1

                if curr_height <= height:
                    break

                top = prev
                width = i - prev - 1
                max_area = max(max_area, width * curr_height)

            if i < n:
                heights[i] = height * base + top + 1
                top = i

        return max_area