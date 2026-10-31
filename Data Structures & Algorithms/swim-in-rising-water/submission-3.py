class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Binary Search + DFS should take O(n^2 log M) time and O(n^2) space where M is the range of possible elevations
        # Since M = N^2, this becomes O(n^2 log n) time and O(n^2) space
        n = len(grid)
        # Want: path from top left to the bottom right where max of the path is minimized
        # 2 * (n - 1)
        low = max(grid[0][0], grid[n-1][n-1])
        high = n * n - 1
        answer = high

        def dfs(elevation, i, j):
            # use stack based dfs to avoid recursion limits
            stack = [(i, j)]
            visited = set()

            while stack:
                i, j = stack.pop()

                if (i, j) in visited:
                    continue
                
                if i < 0 or i > n - 1:
                    continue
                if j < 0 or j > n - 1:
                    continue

                # cannot visit a cell whose elevation is greater than the one given
                if grid[i][j] > elevation:
                    continue
                
                if i == n - 1 and j == n - 1:
                    return True

                visited.add((i, j))
                stack.append((i-1, j))
                stack.append((i+1, j))
                stack.append((i, j-1))
                stack.append((i, j+1))
            return False


        while low <= high:
            mid = low + (high - low) // 2
            if dfs(mid, 0, 0):
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer