class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j, visited):
            if (i, j) in visited:
                return
            
            visited.add((i, j))

            for di, dj in directions:
                ni, nj = i + di, j + dj

                # Seach uphill
                if (0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]):
                    dfs(ni, nj, visited)


        # Pacific: top row and left column
        for i in range(m):
            dfs(i, 0, pacific)

        for j in range(n):
            dfs(0, j, pacific)

        # Atlantic: bottom row and right column
        for i in range(m):
            dfs(i, n - 1, atlantic)

        for j in range(n):
            dfs(m - 1, j, atlantic)
            
        return [list(cell) for cell in pacific.intersection(atlantic)]