class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = []
        num_intervals = len(intervals)
        query_map = {}
        intervals.sort()
        sorted_queries = sorted(queries)

        left = 0
        right = num_intervals - 1
        heap = []

        for query in sorted_queries:
            # Add all intervals that start at or before the query
            while left < num_intervals and intervals[left][0] <= query:
                current_interval = intervals[left]
                foundLength = current_interval[1] - current_interval[0] + 1
                heapq.heappush(heap, (foundLength, current_interval[1]))
                left += 1

            # Remove intervals that end before the query
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            if heap:
                query_map[query] = heap[0][0]
            else:
                query_map[query] = -1

        for query in queries:
            result.append(query_map[query])

        return result