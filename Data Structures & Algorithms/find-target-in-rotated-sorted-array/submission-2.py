class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use binary search starting at the beginning and trying to find the largest number that is larger than first element
        n = len(nums)
        first = nums[0]
        left = 0
        right = n-1
        result_idx = -1
        while (left <= right):
            mid = left + (right - left) // 2
            if first <= nums[mid]:
                result_idx = mid
                left = mid + 1
            else:
                right = mid - 1
        
        rotations = (result_idx + 1) % n
        left = 0
        right = n - 1
        while (left <= right):
            mid = left + (right - left) // 2
            elem = nums[ (mid + rotations) % n ]
            if elem < target:
                left = mid + 1
            elif elem > target:
                right = mid - 1
            else:
                return (mid + rotations) % n
        return -1
            