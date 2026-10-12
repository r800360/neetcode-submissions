class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        dsq_idx = [(points[i][0] ** 2 + points[i][1] ** 2, i) for i in range(n)]
        heapq.heapify(dsq_idx)
        k_closest = heapq.nsmallest(k, dsq_idx)
        return [points[i] for _, i in k_closest]