class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        num_minutes = 0
        trigger = False

        # Run BFS on all rotten fruits
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        while queue:
            for _ in range(len(queue)):
                (i, j) = queue.popleft()
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        trigger = True
                        grid[ni][nj] = 2
                        queue.append((ni, nj))

            if trigger:
                trigger = False
                num_minutes += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return num_minutes