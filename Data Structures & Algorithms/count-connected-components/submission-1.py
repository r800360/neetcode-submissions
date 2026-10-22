class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for first, second in edges:
            graph[first].add(second)
            graph[second].add(first)
        
        # Run DFS on the graph
        visited = [False] * n

        def dfs(node):
            visited[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

            return False

        cc = 0
        for node in range(n):
            if not visited[node]:
                cc += 1
                dfs(node)

        return cc