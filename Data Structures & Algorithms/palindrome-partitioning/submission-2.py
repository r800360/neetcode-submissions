class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        path = []

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            if start == n:
                result.append(path[:])
                return

            for end in range(start, n):
                if not is_palindrome(start, end):
                    continue

                path.append(s[start:end + 1])
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return result