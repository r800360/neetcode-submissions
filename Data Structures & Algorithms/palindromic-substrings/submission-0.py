class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        # Expand outward from each possible center
        for i in range(n):
            # Odd-length palindrome
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            # Even-length palindrome
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        return count