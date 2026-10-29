class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tracks the smallest possible ending value for an increasing subsequence of each length
        tails = []

        for num in nums:
            left, right = 0, len(tails)

            # Find the first index where tails[index] >= num
            while left < right:
                mid = (left + right) // 2

                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)