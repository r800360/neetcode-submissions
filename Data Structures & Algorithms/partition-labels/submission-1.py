class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        # Create a hashtable with the first and last occurrences of each character
        # key: character, value: [firstIdx, lastIdx]
        intervals = {}
        n = len(s)
        for i in range(n):
            if s[i] in intervals:
                intervals[s[i]][1] = i
            else:
                intervals[s[i]] = [i, i]

        left = 0
        right = intervals[s[0]][1]
        for i in range(n):
            intervalLeft, intervalRight = intervals[s[i]]
            # i, left, right, intervalLeft, intervalRight
            if intervalRight > right:
                right = intervalRight
            if i == right:
                # We reached the end and moved the right boundary as far as needed
                result.append(right - left  + 1)
                left = right + 1

        return result