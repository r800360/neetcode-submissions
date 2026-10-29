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
    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # We want to treat the points as vertices in a graph and run Kruskal's MST algorithm using DSU / Union Find
        n = len(points)
        if n <= 1:
            return 0

        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((self.distance(points[i], points[j]), i, j))

        edges.sort()

        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0

        for weight, i, j in edges:
            if uf.union(i, j):
                mst_cost += weight
                edges_used += 1

                if edges_used == n - 1:
                    break

        return mst_cost