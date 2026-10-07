class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        used = [False] * len(nums)

        def dfs():
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                permutation.append(nums[i])

                dfs()

                permutation.pop()
                used[i] = False

        dfs()
        return res