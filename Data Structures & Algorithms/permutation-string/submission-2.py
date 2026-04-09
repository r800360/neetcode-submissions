class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if (n1 > n2):
            return False
        # n1 <= n2 so |s1| <= |s2|
        # Use fixed size arrays for efficiency
        count1 = [0] * 26
        count2 = [0] * 26

        for char in s1:
            count1[ord(char) - ord('a')] += 1

        # set up initial s2 window of size n1
        for i in range(n1):
            count2[ord(s2[i]) - ord('a')] += 1

        if count1 == count2:
            return True

        for i in range(n1, n2):
            # Character entering
            count2[ord(s2[i]) - ord('a')] += 1
            # Character leaving
            count2[ord(s2[i - n1]) - ord('a')] -= 1
            if count1 == count2:
                return True

        return False