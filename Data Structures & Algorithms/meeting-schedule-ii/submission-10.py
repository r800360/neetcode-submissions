"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Greedy and sorting - rooms required is the maximum # of overlapping meetings at any point
        n = len(intervals)
        if n == 0:
            return 0
        if n == 1:
            return 1
        start = sorted(interval.start for interval in intervals)
        end = sorted(interval.end for interval in intervals)
        result = 0
        max_result = 0
        start_ptr = 0
        end_ptr = 0
        while start_ptr < n and end_ptr < n:
            if start[start_ptr] < end[end_ptr]:
                start_ptr += 1
                result += 1
            else:
                end_ptr += 1
                result -= 1
            max_result = max(max_result, result)
        
        return max_result

