class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        n = len(edges) + 1
        for first, second in edges:
            graph[first].add(second)
            graph[second].add(first)

        visited = set()
        path = []
        cycle_edges = set()

        def dfs(node, parent):
            visited.add(node)
            path.append(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if neighbor in visited:
                    # Found a back edge so cycle starts at this previously visited neighbor
                    if neighbor in path:
                        idx = path.index(neighbor)
                        cycle_nodes = path[idx:]

                        for i in range(len(cycle_nodes)):
                            a = cycle_nodes[i]
                            b = cycle_nodes[(i + 1) % len(cycle_nodes)]
                            cycle_edges.add((min(a, b), max(a, b)))

                        return True

                elif dfs(neighbor, node):
                    return True

            path.pop()
            return False

        dfs(1, -1)

        for u, v in reversed(edges):
            if (min(u, v), max(u, v)) in cycle_edges:
                return [u, v]

        return []