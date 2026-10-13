class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n):
            if n == 0:
                return 0, 1

            a, b = fib(n // 2)
            c = a * (2 * b - a)
            d = a * a + b * b

            return (c, d) if n % 2 == 0 else (d, c + d)

        return fib(n + 1)[0]