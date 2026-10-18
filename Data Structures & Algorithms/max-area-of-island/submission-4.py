class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        def dfs(i, j):
            stack = [(i, j)]

            while stack:
                i, j = stack.pop()

                if i < 0 or i >= m:
                    continue

                if j < 0 or j >= n:
                    continue
                
                if grid[i][j] != 1:
                    continue

                grid[i][j] = -1
                self.island_area += 1
                stack.append((i - 1, j))
                stack.append((i + 1, j))
                stack.append((i, j - 1))
                stack.append((i, j + 1))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.island_area = 0
                    dfs(i, j)
                    max_area = max(max_area, self.island_area)

        return max_area