class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        # Adjacency lists will be in lexicographical order
        graph = defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)

        # Run DFS to determine the flight path
        result = []

        def dfs(node):
            while graph[node]:
                neighbor = graph[node].pop()
                dfs(neighbor)
            
            result.append(node)

        dfs("JFK")
        return result[::-1]