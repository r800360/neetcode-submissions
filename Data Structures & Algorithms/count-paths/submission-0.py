class Solution:
    def combination_val(self, n, k):
        # n C k = n!/(k!(n-k)!) = n *** (n - k + 1)/k!
        r = 1
        for i in range(1, k + 1):
            r = r * (n - k + i) // i

        return r

    def uniquePaths(self, m: int, n: int) -> int:
        # m - 1 D letters, n - 1 R letters
        # Answer: (m - 1 + n - 1) C (m - 1) = (m + n - 2) C min(m - 1, n - 1)
        if m > n:
            m, n = n, m
        
        return self.combination_val(m + n - 2, m - 1)

    