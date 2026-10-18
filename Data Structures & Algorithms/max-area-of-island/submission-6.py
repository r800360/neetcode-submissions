class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue

                area = 0
                stack = [(i, j)]
                grid[i][j] = 0  # Mark visited immediately

                while stack:
                    r, c = stack.pop()
                    area += 1

                    for nr, nc in ((r - 1, c), (r + 1, c),
                                   (r, c - 1), (r, c + 1)):
                        if (0 <= nr < m and 0 <= nc < n
                                and grid[nr][nc] == 1):
                            grid[nr][nc] = 0
                            stack.append((nr, nc))

                max_area = max(max_area, area)

        return max_area