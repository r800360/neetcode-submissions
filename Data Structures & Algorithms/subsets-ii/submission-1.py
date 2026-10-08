class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                result.append(subset[:])
                return
            
            # Include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # Skip duplicates in don't include branch
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Don't include nums[i]
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return result