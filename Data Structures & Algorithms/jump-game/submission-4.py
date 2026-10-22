class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # slide right maximally
        right = -1
        for i in range(len(nums)-1):
            right = max(nums[i], right-1)
            if right <= 0:
                return False

        return True