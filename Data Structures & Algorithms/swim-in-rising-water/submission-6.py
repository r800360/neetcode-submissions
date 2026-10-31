class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        min_elevation = [float('inf')] * (n * n)
        min_elevation[0] = grid[0][0]

        pq = [(grid[0][0], 0)]

        while pq:
            current_elevation, u = heapq.heappop(pq)

            if current_elevation > min_elevation[u]:
                continue

            if u == n * n - 1:
                return current_elevation

            r, c = divmod(u, n)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < n and 0 <= nc < n):
                    continue

                v = nr * n + nc

                new_elevation = max(current_elevation, grid[nr][nc])

                if new_elevation < min_elevation[v]:
                    min_elevation[v] = new_elevation
                    heapq.heappush(pq, (new_elevation, v))