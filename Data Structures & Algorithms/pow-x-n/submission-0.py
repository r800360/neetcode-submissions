class Solution:
    def helper(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = self.helper(x, n//2)

        if (n % 2 == 1):
            return x * res * res
        return res * res

    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n *= -1
        
        res = self.helper(x, n//2)

        if (n % 2 == 1):
            return x * res * res
        return res * res