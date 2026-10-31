class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)

        prev = [False] * (n + 1)
        prev[0] = True

        # Initialize empty string matches - empty string can match like a*b*b*
        for j in range(2, n + 1):
            if p[j - 1] == "*":
                prev[j] = prev[j-2]

        for char in s:
            curr = [False] * (n + 1)
            for j in range(1, n+1):
                # pattern contains *
                if p[j - 1] == "*":
                    curr[j] = curr[j-2]
                    # parse previous literal
                    if p[j - 2] == "." or p[j - 2] == char:
                        curr[j] |= prev[j]
                # parse normal literal
                elif p[j - 1] == "." or p[j - 1] == char:
                    curr[j] = prev[j - 1]

            prev = curr

        return prev[n]