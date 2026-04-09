class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        char_counts = defaultdict(int)
        maxWindowSize = 0
        currWindowSize = 0
        left = 0
        for right in range(n):
            char_counts[s[right]] += 1
            currWindowSize += 1
            
            # remove duplicate
            while (char_counts[s[right]] > 1):
                char_counts[s[left]] -= 1
                currWindowSize -= 1
                left += 1

            maxWindowSize = max(maxWindowSize, currWindowSize)

        return maxWindowSize