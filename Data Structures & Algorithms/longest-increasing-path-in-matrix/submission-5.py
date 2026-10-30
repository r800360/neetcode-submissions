class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # Think of the matrix as a graph with directed edges for strictly increasing adjacent
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
                    graph[(i,j)].append((i-1, j))
                    indegree[(i-1, j)] += 1
                if i + 1 < m and matrix[i][j] < matrix[i + 1][j]:
                    graph[(i,j)].append((i+1, j))
                    indegree[(i+1, j)] += 1
                if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                    graph[(i,j)].append((i, j-1))
                    indegree[(i, j-1)] += 1
                if j + 1 < n and matrix[i][j] < matrix[i][j + 1]:
                    graph[(i,j)].append((i, j+1))
                    indegree[(i, j+1)] += 1

        # Get the longest path in graph using Kahn's algorithm
        queue = deque(key for key in graph if indegree[key] == 0)
        dp = [1] * (m * n)

        while queue:
            i, j = queue.popleft()

            for u, v in graph[(i, j)]:
                dp[u * n + v] = max(dp[u * n + v], dp[i * n + j] + 1)

                indegree[(u, v)] -= 1
                if indegree[(u, v)] == 0:
                    queue.append((u,v))
        
        return max(dp)