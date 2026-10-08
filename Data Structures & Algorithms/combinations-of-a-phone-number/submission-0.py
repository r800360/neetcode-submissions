class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_chars = {}
        digit_chars["2"] = "abc"
        digit_chars["3"] = "def"
        digit_chars["4"] = "ghi"
        digit_chars["5"] = "jkl"
        digit_chars["6"] = "mno"
        digit_chars["7"] = "pqrs"
        digit_chars["8"] = "tuv"
        digit_chars["9"] = "wxyz"

        result = []

        def backtrack(rem_digits, current):
            if not rem_digits:
                result.append(current)
                return
            chars = digit_chars[rem_digits[0]]
            for i in range(len(chars)):
                backtrack(rem_digits[1:], current + chars[i])

        backtrack(digits, "")
        return result