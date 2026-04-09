class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        window_counts = [0] * 26
        maxWindowSize = 0
        left = 0

        for right in range(n):
            window_counts[ord(s[right]) - ord('A')] += 1

            while ((right - left + 1) - max(window_counts) > k):
                window_counts[ord(s[left]) - ord('A')] -= 1
                left += 1
            maxWindowSize = max(maxWindowSize, right - left + 1)

        return maxWindowSize