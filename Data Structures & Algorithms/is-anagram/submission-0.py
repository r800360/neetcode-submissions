class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_counts = defaultdict(int)
        for i, char in enumerate(s):
            char_counts[char] += 1
        for i, char in enumerate(t):
            char_counts[char] -= 1
        for i in char_counts.values():
            if i != 0:
                return False
        return True