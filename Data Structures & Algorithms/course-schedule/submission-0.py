class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for prerequisite in prerequisites:
            graph[prerequisite[1]].add(prerequisite[0])
        
        # Use DFS to check if graph has cycle; if DAG return true otherwise return false
        colors = [0] * numCourses
        
        def has_cycle(node):
            colors[node] = 1
            
            for neighbor in graph[node]:
                if colors[neighbor] == 1:
                    return True
                
                if colors[neighbor] == 0 and has_cycle(neighbor):
                    return True
            
            colors[node] = 2
            return False
        
        for i in range(numCourses):
            if colors[i] == 0 and has_cycle(i):
                # Has a cycle
                return False

        return True