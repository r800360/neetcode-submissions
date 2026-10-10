class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(len(s)) time and O(1) space
        # two pointers
        left = 0
        right = len(s)-1

        while left < right:
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(i, slist):
            if i == len(s):
                if self.isPalindrome(slist[-1]):
                    result.append(slist[:])
                return

            # continue without partitioning
            slist[-1] += s[i]
            backtrack(i+1, slist)
            slist[-1] = slist[-1][:-1]

            # partition and start a new string
            if not self.isPalindrome(slist[-1]):
                return
            slist.append(s[i])
            backtrack(i+1, slist)
            slist.pop()

        backtrack(1, [s[0]])
        return result