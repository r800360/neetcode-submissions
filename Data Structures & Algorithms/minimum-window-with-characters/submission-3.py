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
        left = 0
        chars_needed = t_len

        min_len = float("inf")
        min_start = 0

        for right in range(s_len):
            right_idx = ord(s[right]) - ord('A')
            window_counts[right_idx] += 1

            # If this character was still needed, we satisfied one requirement
            if t_counts[right_idx] > 0 and window_counts[right_idx] <= t_counts[right_idx]:
                chars_needed -= 1

            # Once all required chars are included, shrink from the left
            while chars_needed == 0:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_start = left

                left_idx = ord(s[left]) - ord('A')
                window_counts[left_idx] -= 1

                # If removing s[left] makes us lose a required char, window becomes invalid
                if t_counts[left_idx] > 0 and window_counts[left_idx] < t_counts[left_idx]:
                    chars_needed += 1

                left += 1

        return "" if min_len == float("inf") else s[min_start:min_start + min_len]