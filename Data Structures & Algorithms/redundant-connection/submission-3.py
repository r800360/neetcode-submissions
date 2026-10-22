class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = [[] for _ in range(n+1)]
        degree = [0] * (n+1)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
            degree[v1] += 1
            degree[v2] += 1

        dq = deque()
        for node in range(1, n+1):
            if degree[node] == 1:
                dq.append(node)
        while dq:
            node = dq.popleft()
            degree[node] -= 1
            for nei in adj[node]:
                if degree[nei] > 0:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        dq.append(nei)

        for i in range(n-1, -1, -1):
            u, v = edges[i]
            if degree[u] == 2 and degree[v] == 2:
                return [u, v]
        return []