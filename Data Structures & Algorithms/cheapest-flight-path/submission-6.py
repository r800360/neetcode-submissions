class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Idea: Try using Bellman-Ford
        dist = [float("inf")] * n
        dist[src] = 0

        # At most k stops = At most k + 1 flights
        for _ in range(k + 1):
            # copy previous distances
            temp_dist = dist.copy()

            # relax every edge
            for u, v, price in flights:
                if dist[u] != float("inf"):
                    temp_dist[v] = min(temp_dist[v], dist[u] + price)

            # restore
            dist = temp_dist

        result = dist[dst]
        if result == float("inf"):
            return -1
        return result