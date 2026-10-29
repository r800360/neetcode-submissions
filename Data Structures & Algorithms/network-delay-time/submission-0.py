class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(set)
        for u, v, t in times:
            graph[u].add((v, t))
        
        # Run Dijkstra's shortest path algorithm
        min_dist = [float("inf")] * (n + 1)
        min_dist[0] = -10
        min_dist[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            current_dist, u = heapq.heappop(pq)

            if current_dist > min_dist[u]:
                continue

            for v, t in graph[u]:
                new_dist = current_dist + t
                if new_dist < min_dist[v]:
                    min_dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))
        
        result = max(min_dist)

        if result == float("inf"):
            return -1
        
        return result