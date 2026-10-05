class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powTwo = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        n = len(nums)
        result = []
        for i in range(powTwo[n]):
            # bitwise representation of i; 0 -> exclude index, 1 -> include index
            # 000 -> [], 010 -> [2], 011 -> [2, 3]
            subset = []
            for k in range(n):
                if ((i >> k) & 1):
                    subset.append(nums[k])

            result.append(subset)
        return result
