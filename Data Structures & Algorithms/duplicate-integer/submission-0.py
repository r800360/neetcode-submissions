class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for i, num in enumerate(nums):
            if (count[num] != 0):
                return True
            count[num] += 1
        return False