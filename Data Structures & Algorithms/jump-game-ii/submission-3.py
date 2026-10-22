class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        min_jumps = 0

        while right < n - 1:
            farthest_value = right
            
            for i in range(left, right+1):
                if i < n:
                    farthest_value = max(farthest_value, i + nums[i])
            
            min_jumps += 1
            left = right + 1
            right = farthest_value
        
        return min_jumps