class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:
                return True
            seen.add(n)
            first = n % 10
            second = n // 10 % 10
            third = n // 100 % 10
            fourth = n // 1000 % 10
            n = first * first + second * second + third * third + fourth * fourth
            if n in seen:
                return False