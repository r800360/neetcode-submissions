class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        
        def dfs(combination, remainder, start):
            if remainder < 0:
                return
            if remainder == 0:
                result.append(combination[:])
                return
            
            for i in range(start, n):
                num = nums[i]
                combination.append(num)
                dfs(combination, remainder-num, i)
                combination.pop()

        dfs([], target, 0)
        return result