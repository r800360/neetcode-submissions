class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def backtrack(left, right):
            if left == n and right == n:
                result.append("".join(path))
                return
            
            if left < n:
                path.append("(")
                backtrack(left + 1, right)
                path.pop()

            if right < left:
                path.append(")")
                backtrack(left, right + 1)
                path.pop()

        backtrack(0, 0)
        return result