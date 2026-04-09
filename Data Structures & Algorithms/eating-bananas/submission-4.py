class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        # If k = 1, sum_i piles[i] = total number of hours
        # If k = 2, sum_i ceil(piles[i]/2)
        # If k = n, sum_i ceil(piles[i]/n) = total number of hours
        # Problem: Find min k such that sum_i ceil(piles[i]/k) < given h
        # Use binary search
        left = 1
        right = max(piles)
        answer = right

        while (left <= right):
            k = left + (right - left)//2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile/k)
            
            if (total_hours > h):
                # Taking too long, increase eating speed
                left = k + 1
            else:
                # total_hours <= h, so k works; try smaller
                answer = k
                right = k - 1
        return answer