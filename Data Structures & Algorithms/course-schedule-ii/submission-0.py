class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for prerequisite in prerequisites:
            graph[prerequisite[1]].add(prerequisite[0])
        
        # Run Kahn's algorithm to get a valid ordering of courses
        indegree = [0] * numCourses

        for course in range(numCourses):
            for post in graph[course]:
                indegree[post] += 1

        queue = deque(course for course in range(numCourses) if indegree[course] == 0)
        processed = 0
        result = []

        while queue:
            course = queue.popleft()
            processed += 1
            result.append(course)

            for post in graph[course]:
                indegree[post] -= 1

                if indegree[post] == 0:
                    queue.append(post)

        if processed != numCourses:
            return []

        return result