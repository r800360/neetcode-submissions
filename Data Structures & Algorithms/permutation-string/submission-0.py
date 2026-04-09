class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if (n1 > n2):
            return False
        # n1 <= n2 so |s1| <= |s2|
        # Sliding Window Problem - O(n2) time and O(1) space
        # Window Size must be n1
        count_s1 = defaultdict(int)
        for char in s1:
            count_s1[char] += 1
        
        comp_dict = defaultdict(int)
        for i in range(len(s2)-len(s1)+1):
            start = i
            end = i + n1
            for j in range(start, end):
                comp_dict[s2[j]] += 1
            if (comp_dict == count_s1):
                return True
            comp_dict.clear()
        return False