class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(curr, left, right):
            if len(curr) == 2 * n:
                result.append(curr)
                return

            if left < n:
                backtrack(curr + "(", left + 1, right)

            if right < left:
                backtrack(curr + ")", left, right + 1)

        backtrack("", 0, 0)
        return result