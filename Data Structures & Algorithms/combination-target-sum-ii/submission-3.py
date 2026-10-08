class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        candidates.sort()

        def backtrack(combination, remainder, start):
            if remainder < 0:
                return
            if remainder == 0:
                result.append(combination[:])
                return
            
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                num = candidates[i]
                combination.append(num)
                backtrack(combination, remainder-num, i+1)
                combination.pop()

        backtrack([], target, 0)
        return result