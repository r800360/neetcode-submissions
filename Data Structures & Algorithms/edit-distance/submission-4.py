class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        # Levenshtein distance
        m = len(word1)
        n = len(word2)
        lev_dist = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            lev_dist[i][0] = i

        for j in range(n + 1):
            lev_dist[0][j] = j

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    subCost = 0
                else:
                    subCost = 1

                lev_dist[i + 1][j + 1] = min(
                    lev_dist[i][j + 1] + 1,
                    lev_dist[i + 1][j] + 1,
                    lev_dist[i][j] + subCost
                )
        
        return lev_dist[m][n]
