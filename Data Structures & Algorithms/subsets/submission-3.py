class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for i in range(2**n):
            # bitwise representation of i; 0 -> exclude index, 1 -> include index
            # 000 -> [], 010 -> [2], 011 -> [2, 3]
            subset = []
            for k in range(n):
                if ((i >> k) & 1):
                    subset.append(nums[k])

            result.append(subset)
        return result