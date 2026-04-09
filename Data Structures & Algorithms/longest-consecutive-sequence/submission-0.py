class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longestStreak = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                currentNum = num
                currentStreak = 1

                while (currentNum + 1) in nums_set:
                    currentNum += 1
                    currentStreak += 1

                longestStreak = max(longestStreak, currentStreak)
        
        return longestStreak
