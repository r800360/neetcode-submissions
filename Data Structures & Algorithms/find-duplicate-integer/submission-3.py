class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        
        second_slow = 0
        while True:
            slow = nums[slow]
            second_slow = nums[second_slow]

            if slow == second_slow:
                return slow

        return 0