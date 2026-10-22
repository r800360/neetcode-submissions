class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for first, second in edges:
            graph[first].add(second)
            graph[second].add(first)
        
        # If the graph is connected and acyclic, then it is a tree
        visited = [False] * n

        def dfs(node, parent):
            visited[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True

            return False

        if dfs(0, -1):
            return False
        
        return all(visited)