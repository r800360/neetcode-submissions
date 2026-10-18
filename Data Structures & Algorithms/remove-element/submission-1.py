class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] == val:
                for j in range(i, n-1):
                    nums[j] = nums[j + 1]
            else:
                k += 1

        return k