class Solution:
    def countSubstrings(self, s: str) -> int:
        # Transform s to handle odd/even palindromes uniformly.
        # Example: "abba" -> "^#a#b#b#a#$"
        t = "^#" + "#".join(s) + "#$"
        n = len(t)

        # p[i] = radius of the palindrome centered at i
        p = [0] * n
        center = right = 0
        count = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            # Reuse the known palindrome information when possible.
            if i < right:
                p[i] = min(right - i, p[mirror])

            # Expand around i while the characters match.
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            # Update the rightmost palindrome.
            if i + p[i] > right:
                center = i
                right = i + p[i]

            count += (p[i] + 1) // 2

        return count