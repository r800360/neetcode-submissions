class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        t_len = len(t)
        if (t_len > s_len):
            return ""
        
        t_counts = [0] * 58
        for char in t:
            t_counts[ord(char) - ord('A')] += 1
        
        # Sliding Window
        # Set up an initial window of size t_len in s
        window_counts = [0] * 58
        for i in range(t_len):
            window_counts[ord(s[i]) - ord('A')] += 1

        if all(t_counts[i] <= window_counts[i] for i in range(58)):
            return s[:t_len]
        
        minSubstring = ""
        left = 0

        # We want t_counts <= window_counts (needs to contain everything in t_counts)
        for right in range(t_len, s_len):
            window_counts[ord(s[right]) - ord('A')] += 1
            while (all(t_counts[i] <= window_counts[i] for i in range(58))):
                # Window contains t
                if minSubstring == "" or (right - left + 1 < len(minSubstring)):
                    minSubstring = s[left:right+1]

                window_counts[ord(s[left]) - ord('A')] -= 1
                left += 1

        return minSubstring
