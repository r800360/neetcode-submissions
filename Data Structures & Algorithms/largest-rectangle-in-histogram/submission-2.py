class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        # if height monotonically decreases, then the algorithm is correct
        # therefore, the stack (somehow) handles increases in height
        for i, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > height:
                stack_height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, width * stack_height)
            
            stack.append(i)
        return max_area