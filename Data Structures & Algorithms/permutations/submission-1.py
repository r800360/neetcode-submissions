class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            new_res = []

            for perm in res:
                for i in range(len(perm) + 1):
                    new_res.append(perm[:i] + [num] + perm[i:])

            res = new_res

        return res