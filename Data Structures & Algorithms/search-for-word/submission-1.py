class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        word_len = len(word)

        def dfs(i, j, k):
            if k >= word_len:
                return True
            
            if i < 0 or i >= m:
                return False

            if j < 0 or j >= n:
                return False

            if board[i][j] != word[k]:
                return False
            
            board[i][j] = "."

            found = dfs(i-1, j, k+1) or dfs(i + 1, j, k+1) or dfs(i, j-1, k+1) or dfs(i, j+1, k+1)

            board[i][j] = word[k]

            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False