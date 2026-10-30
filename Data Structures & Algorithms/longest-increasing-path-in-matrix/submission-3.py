class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        indegree = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for di, dj in directions:
                    ni, nj = i + di, j + dj

                    if 0 <= ni < m and 0 <= nj < n:
                        if matrix[ni][nj] < matrix[i][j]:
                            indegree[i][j] += 1

        queue = deque()

        for i in range(m):
            for j in range(n):
                if indegree[i][j] == 0:
                    queue.append((i, j))

        dp = [[1] * n for _ in range(m)]
        ans = 1

        while queue:
            i, j = queue.popleft()
            ans = max(ans, dp[i][j])

            for di, dj in directions:
                ni, nj = i + di, j + dj

                if 0 <= ni < m and 0 <= nj < n:
                    if matrix[ni][nj] > matrix[i][j]:
                        dp[ni][nj] = max(
                            dp[ni][nj],
                            dp[i][j] + 1
                        )

                        indegree[ni][nj] -= 1

                        if indegree[ni][nj] == 0:
                            queue.append((ni, nj))

        return ans