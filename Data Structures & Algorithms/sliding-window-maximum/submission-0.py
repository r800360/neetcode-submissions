class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Naive approach O(nk) time and O(n-k) space
        n = len(nums)
        left = 0
        result = [0] * (n-k+1)
        
        # Set up initial sliding window
        window_max = -10001

        for i in range(k):
            window_max = max(window_max, nums[i])

        result[0] = window_max
        left += 1

        for i in range(k, n):
            window_max = -10001
            for j in range(left, i+1):
                window_max = max(window_max, nums[j])
            result[i-(k-1)] = window_max
            left += 1
            # Admitting element less than window_max
            
            
        return result
