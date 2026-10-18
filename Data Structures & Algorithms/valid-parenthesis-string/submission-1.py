class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []

        for i in range(len(s)):
            c = s[i]
            if c == ')':
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            elif c == '(':
                left_stack.append(i)
            else:
                star_stack.append(i)


        # If I take s and I remove the indices, there are no right parenthesis left
        # star_stack and the left_stack have all the remaining info
        if len(left_stack) > len(star_stack):
            return False

        while left_stack:
            if left_stack[-1] >= star_stack[-1]:
                return False
            else:
                left_stack.pop()
                star_stack.pop()
        
        return True

        