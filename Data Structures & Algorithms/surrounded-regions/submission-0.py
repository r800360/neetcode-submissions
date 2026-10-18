class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def dfs_read(i, j):
            stack = [(i, j)]

            while stack:
                i, j = stack.pop()

                if i < 0 or i >= m:
                    continue

                if j < 0 or j >= n:
                    continue

                if board[i][j] != 'O':
                    continue

                # Mark cell as safe so we do not revisit it
                board[i][j] = 'S'

                stack.append((i - 1, j))
                stack.append((i + 1, j))
                stack.append((i, j - 1))
                stack.append((i, j + 1))

        for i in range(m):
            dfs_read(i, 0)
            dfs_read(i, n - 1)

        for j in range(n):
            dfs_read(0, j)
            dfs_read(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
                