class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        subsets = self.subsets(nums[1:])

        return subsets + [subset + [nums[0]] for subset in subsets]