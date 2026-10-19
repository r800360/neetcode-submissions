class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # slide right maximally
        right = -1
        for i in range(len(nums)-1):
            right -= 1
            right = max(nums[i], right)
            if right > 0:
                i += 1
            else:
                return False

        return True