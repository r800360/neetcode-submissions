class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        minHeap = [[grid[0][0], 0, 0]] ## [maxHeight seen so far, row index, col index]
        visit = set()
        visit.add((0,0))
        
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        while minHeap:
            maxH, r, c = heapq.heappop(minHeap)

            if r == N - 1 and c == N - 1:
                return maxH
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= N or nc >= N or (nr, nc) in visit:
                    continue
                visit.add((nr, nc))
                heapq.heappush(minHeap, [max(maxH, grid[nr][nc]), nr, nc])
        