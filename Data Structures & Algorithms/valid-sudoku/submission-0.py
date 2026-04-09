class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counts = defaultdict(int)
        n = range(len(board[0]))

        # check rows
        for row in board:
            for num in row:
                if num == ".":
                    continue
                if (counts[num] != 0):
                    return False
                counts[num] += 1
            counts.clear()

        # check columns
        for col in n:
            for i in n:
                element = board[i][col]
                if (element == "."):
                    continue
                if (counts[element] != 0):
                    return False
                counts[element] += 1
            counts.clear()

        # 3 by 3 sub-box check
        for box in n:
            for i in n:
                element = board[3 * (box // 3) + i // 3][3 * (box % 3) + i % 3]
                if (element == "."):
                    continue
                if (counts[element] != 0):
                    return False
                counts[element] += 1
            counts.clear()

        return True