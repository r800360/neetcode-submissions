class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        newIntervalStart, newIntervalEnd = newInterval
        left = 0
        right = n - 1
        while left < n and newIntervalStart > intervals[left][1]:
            left += 1
        if left >= n:
            return intervals + [newInterval]
        while right >= 0 and newIntervalEnd < intervals[right][0]:
            right -= 1
        if right < 0:
            return [newInterval] + intervals
        
        # 0 <= left, right < n
        # newIntervalStart <= intervals[left][1], intervals[right][0] <= newIntervalEnd
        if left > right:
            intervals.insert(left, newInterval)
        else:
            # remove left, left + 1, ..., right and then insert at left
            newLeft = min(newIntervalStart, intervals[left][0])
            newRight = max(newIntervalEnd, intervals[right][1])
            del intervals[left : right + 1]
            intervals.insert(left, [newLeft, newRight])

        return intervals