class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Binary Search + DFS should take O(n^2 log M) time and O(n^2) space where M is the range of possible elevations
        # Since M = N^2, this becomes O(n^2 log n) time and O(n^2) space
        n = len(grid)
        # Want: path from top left to the bottom right where max of the path is minimized
        # 2 * (n - 1)
        low = max(grid[0][0], grid[n-1][n-1])
        high = n * n - 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(elevation):
            stack = [(0, 0)]
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            while stack:
                r, c = stack.pop()

                if (r, c) == (n - 1, n - 1):
                    return True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if not (0 <= nr < n and 0 <= nc < n):
                        continue

                    if visited[nr][nc]:
                        continue

                    if grid[nr][nc] > elevation:
                        continue

                    visited[nr][nc] = True
                    stack.append((nr, nc))

            return False


        while low <= high:
            mid = low + (high - low) // 2
            if dfs(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low