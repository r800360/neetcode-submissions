class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = 0, len(intervals) - 1
        start, end = newInterval

        while left <= right and intervals[left][1] < start:
            left += 1

        while right >= left and intervals[right][0] > end:
            right -= 1

        if left <= right:
            newInterval = [
                min(start, intervals[left][0]),
                max(end, intervals[right][1])
            ]

        intervals[left:right + 1] = [newInterval]
        return intervals