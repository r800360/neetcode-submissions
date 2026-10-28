class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted(queries)

        result = {}
        heap = []
        i = 0
        n = len(intervals)

        for q in sorted_queries:
            while i < n and intervals[i][0] <= q:
                start, end = intervals[i]
                heapq.heappush(heap, (end - start + 1, end))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            result[q] = heap[0][0] if heap else -1

        return [result[q] for q in queries]