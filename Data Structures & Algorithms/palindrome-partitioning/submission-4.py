class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []
        path = []

        # is_palindrome[i][j] indicates whether s[i:j+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]

        # Precompute all palindrome substrings in O(n^2) time
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (
                    j - i <= 2 or is_palindrome[i + 1][j - 1]
                ):
                    is_palindrome[i][j] = True

        def backtrack(start: int) -> None:
            if start == n:
                result.append(path[:])
                return

            for end in range(start, n):
                if not is_palindrome[start][end]:
                    continue

                # Choose
                path.append(s[start:end + 1])

                # Explore
                backtrack(end + 1)

                # Unchoose
                path.pop()

        backtrack(0)
        return result