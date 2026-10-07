class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        n = len(nums)

        def dfs(permutation):
            if len(permutation) == n:
                permutations.append(permutation[:])
                return

            for i in range(len(nums)):
                num = nums[i]
                nums.pop(i)
                permutation.append(num)
                dfs(permutation)
                nums.insert(i, num)
                permutation.pop()

        dfs([])
        return permutations