class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        for u, v, p in flights:
            graph[u].add((v, p))
        
        # Run Dijkstra's shortest path algorithm with min_dist[node][num_stops]
        min_dist = [[float("inf") for _ in range(k+2)] for _ in range(n)]
        min_dist[src][0] = 0
        pq = []
        heapq.heappush(pq, (0, src, 0))

        while pq:
            current_price, u, stops = heapq.heappop(pq)

            if stops == k + 1:
                continue

            if current_price > min_dist[u][stops]:
                continue

            for v, p in graph[u]:
                # don't throw away paths that cost more with fewer stops remaining
                new_price = current_price + p
                if new_price < min_dist[v][stops + 1]:
                    min_dist[v][stops + 1] = new_price
                    heapq.heappush(pq, (new_price, v, stops + 1))

        result = min(min_dist[dst])
        
        if result == float("inf"):
            return -1

        return result