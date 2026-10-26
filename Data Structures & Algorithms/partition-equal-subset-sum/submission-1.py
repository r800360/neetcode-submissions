class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sum_nums = 0
        for num in nums:
            sum_nums += num

        if sum_nums % 2 == 1:
            return False

        # sum of all the elements in the array is even
        subset_sum = sum_nums // 2

        # It suffices to check every subset less than or equal to length n / 2
        # If any sum goes over subset_sum then it does not work
        # formable_sums = [0] * (subset_sum + 1)

        def backtrack(i, curr_sum):
            if i >= n:
                return False
            if curr_sum > subset_sum:
                return False
            if curr_sum == subset_sum:
                return True

            return backtrack(i + 1, curr_sum + nums[i]) or backtrack(i + 1, curr_sum)
        
        
        return backtrack(0, 0)