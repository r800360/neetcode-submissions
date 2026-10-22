class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for first, second in edges:
            graph[first].add(second)
            graph[second].add(first)
        
        # If the graph is connected and acyclic, then it is a tree
        visited = [False] * n

        def bfs(start):
            queue = deque()
            queue.append([start, -1])
            visited[start] = True

            while queue:
                node, parent = queue.popleft()

                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append([neighbor, node])
                    elif neighbor != parent:
                        return True

            return False

        if bfs(0):
            return False
        
        return all(visited)