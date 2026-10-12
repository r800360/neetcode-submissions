class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        self.nums = nums

        for num in nums:
            heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        k = self.k
        heap = self.heap
        while len(heap) > k:
            heapq.heappop(heap)
        
        heapq.heappush(heap, val)
        while len(heap) > k:
            heapq.heappop(heap)
        return heap[0]
