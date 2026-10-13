class Solution:
    def climbStairs(self, n: int) -> int:
        alpha = (1 + math.sqrt(5))/2
        beta = (1 - math.sqrt(5))/2

        return round(( alpha ** (n+1) + beta ** (n+1) )/math.sqrt(5) )