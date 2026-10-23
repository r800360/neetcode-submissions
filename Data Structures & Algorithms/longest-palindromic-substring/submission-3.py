class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        n = len(s)

        # Expand outward from each possible center
        for i in range(n):
            # Odd-length palindrome
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left : right + 1]
                left -= 1
                right += 1

            # Even-length palindrome
            left, right = i, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left : right + 1]
                left -= 1
                right += 1

        return result