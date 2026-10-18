class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        def dfs(i, j):
            if i < 0 or i >= m:
                return

            if j < 0 or j >= n:
                return
            
            if grid[i][j] != 1:
                return

            grid[i][j] = -1
            self.island_area += 1
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.island_area = 0
                    dfs(i, j)
                    max_area = max(max_area, self.island_area)

        return max_area