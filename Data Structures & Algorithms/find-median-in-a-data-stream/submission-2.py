class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        # use binary search to add the number
        left = 0
        right = len(self.stream)

        while left < right:
            mid = left + (right - left) // 2
            if self.stream[mid] < num:
                left = mid + 1
            else:
                right = mid

        self.stream.insert(left, num)

    def findMedian(self) -> float:
        n = len(self.stream)
        if n % 2 == 0:
            return (self.stream[n//2] + self.stream[n//2 - 1])/2
        else:
            return self.stream[(n - 1) // 2]
        