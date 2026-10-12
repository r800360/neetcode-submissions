class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            largest = -heapq.heappop(max_heap)
            second_largest = -heapq.heappop(max_heap)
           
            if largest > second_largest:
                heapq.heappush(max_heap, second_largest - largest)

        if len(max_heap) == 1:
            return -max_heap[0]

        return 0