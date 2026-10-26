class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        second = 1
        third = 1
        if n == 0:
            return first
        if n == 1:
            return second
        if n == 2:
            return third

        for _ in range(n - 2):
            first, second, third = second, third, first + second + third

        return third