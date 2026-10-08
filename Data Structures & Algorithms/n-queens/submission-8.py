class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        positions = [0] * n
        full = (1 << n) - 1

        def backtrack(row, cols, diag1, diag2):
            if row == n:
                result.append([
                    "." * col + "Q" + "." * (n - col - 1)
                    for col in positions
                ])
                return

            available = full & ~(cols | diag1 | diag2)

            while available:
                bit = available & -available
                available ^= bit

                col = bit.bit_length() - 1
                positions[row] = col

                backtrack(
                    row + 1,
                    cols | bit,
                    ((diag1 | bit) << 1) & full,
                    (diag2 | bit) >> 1
                )

        backtrack(0, 0, 0, 0)
        return result