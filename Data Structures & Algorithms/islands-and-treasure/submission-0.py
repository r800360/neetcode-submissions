class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Run BFS
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        counter = 1
        while queue:
            for _ in range(len(queue)):
                (i, j) = queue.popleft()
                for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 2147483647:
                            grid[ni][nj] = counter
                            queue.append((ni, nj))

            counter += 1