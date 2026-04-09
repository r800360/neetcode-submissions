class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean the string
        s = ''.join([char for char in s if char.isalnum()])
        s = s.lower()

        # two pointers
        left = 0
        right = len(s)-1
        while left < right:
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        
        return True
