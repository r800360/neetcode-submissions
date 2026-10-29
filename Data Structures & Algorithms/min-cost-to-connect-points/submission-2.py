class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Since the graph is really dense, Prim's algorithm is more optimal than Kruskal's algorithm
        n = len(points)
        if n <= 1:
            return 0

        min_dist = [float("inf")] * n
        visited = [False] * n
        min_dist[0] = 0

        total_cost = 0

        for _ in range(n):
            # Find the cheapest unvisited point
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            visited[u] = True
            total_cost += min_dist[u]

            # Update connection costs to remaining points
            x1, y1 = points[u]
            for v in range(n):
                if not visited[v]:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    min_dist[v] = min(min_dist[v], dist)

        return total_cost