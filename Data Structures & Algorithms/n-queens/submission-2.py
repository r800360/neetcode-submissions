class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["." for _ in range(n)] for _ in range(n)]

        def backtrack(board, queens_left, i, j):
            if queens_left == 0:
                result.append(["".join(row) for row in board])
                return
            if i >= n or j >= n:
                return
            
            # check if it is safe to place the queen
            # check row
            for col in range(n):
                if board[i][col] == "Q":
                    backtrack(board, queens_left, i+1, 0)
                    return

            # check col
            for row in range(n):
                if board[row][j] == "Q":
                    backtrack(board, queens_left, i, j+1)
                    return
            
            # check diag - [i +- k][j +- k]
            k = 1
            while k <= n:
                candidates = [(i-k, j-k), (i-k, j+k), (i+k, j-k), (i+k, j+k)]
                for (testI, testJ) in candidates:
                    if testI < 0 or testI >= n or testJ < 0 or testJ >= n:
                        continue
                    if board[testI][testJ] == "Q":
                        backtrack(board, queens_left, i, j+1)
                        return

                k += 1
            
            board[i][j] = "Q"
            backtrack(board, queens_left-1, i+1, 0)
            board[i][j] = "."
            backtrack(board, queens_left, i, j+1)

        backtrack(board, n, 0, 0)
        return result