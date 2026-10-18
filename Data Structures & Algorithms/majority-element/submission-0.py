class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = -1
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                if num == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate