class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rowSet = set()
        colSet = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)

        for row in rowSet:
            for j in range(n):
                matrix[row][j] = 0

        for col in colSet:
            for i in range(m):
                matrix[i][col] = 0        