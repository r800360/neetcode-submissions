class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Idea - Union Find
        # sort cells by elevation
        # gradually activate cells as water level increases
        # connect neighboring active cells
        # determine whether the starting and ending cells have become connected
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        indices = [(i, j) for i in range(n) for j in range(n)]
        sorted_indices = sorted(indices, key=lambda idx:grid[idx[0]][idx[1]])
        active = [False] * (n * n)
        uf = UnionFind(n*n)
        result = 0

        for r, c in sorted_indices:
            # raise the water level up to the elevation at this index, then check if start, end have become connected
            result = grid[r][c]
            current = r * n + c
            active[current] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < n and 0 <= nc < n):
                    continue
                
                neighbor = nr * n + nc

                if active[neighbor]:
                    uf.union(current, neighbor)

            if uf.find(0) == uf.find(n * n - 1):
                return result

        return result