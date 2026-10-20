class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy and sorting
        if len(intervals) == 1:
            return 0
        min_intervals = 0
        intervals.sort(reverse = True)
        while intervals:
            first = intervals.pop()
            if not intervals:
                break
            second = intervals[-1]
            if first[1] > second[0]:
                min_intervals += 1
                # Intervals overlap so we need to remove the one stretching furthest right and add back the other
                intervals.pop()
                if first[1] > second[1]:
                    # remove first and add back second
                    intervals.append(second)
                else:
                    # remove second and add back first
                    intervals.append(first)

        return min_intervals