class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = 0
        result = []
        direction = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while len(result) < m * n:
            result.append(matrix[i][j])
            matrix[i][j] = 404

            di, dj = dirs[direction]
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] != 404:
                i, j = ni, nj
            else:
                direction = (direction + 1) % 4
                di, dj = dirs[direction]
                i += di
                j += dj

        return result
