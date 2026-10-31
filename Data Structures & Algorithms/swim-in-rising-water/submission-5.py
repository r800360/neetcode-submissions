class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Dijkstra - minimum possible maximum elevation required to reach each cell
        # Traditional Dijkstra minimizes sum of edge weights but here we want to minimize
        # the maximum elevation along a path
        # O(n^2 log n) time and O(n^2) space
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_elevation = [n * n - 1] * (n * n)
        init_elevation = grid[0][0]
        max_elevation[0] = init_elevation
        pq = []
        heapq.heappush(pq, (init_elevation, 0))

        while pq:
            current_elevation, u = heapq.heappop(pq)

            if current_elevation > max_elevation[u]:
                continue

            i = u // n
            j = u % n
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if not (0 <= ni < n and 0 <= nj < n):
                    continue
                v = ni * n + nj
                weight = max(grid[i][j], grid[ni][nj])
                new_elevation = max(weight, current_elevation)
                if new_elevation < max_elevation[v]:
                    max_elevation[v] = new_elevation
                    heapq.heappush(pq, (new_elevation, v))
                          
        return max_elevation[-1]

        