class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # largest timestamp_prev < timestamp given as an argument
        if key not in self.timeMap:
            return ""

        value_timestamp = self.timeMap[key]
        num_values = len(value_timestamp)
        left = 0
        right = num_values - 1
        result_idx = -1
        while (left <= right):
            mid = left + (right - left) // 2
            mid_timestamp = value_timestamp[mid][1]
            if mid_timestamp <= timestamp:
                result_idx = mid
                left = mid + 1
            else:
                right = mid - 1

        return value_timestamp[result_idx][0] if result_idx != -1 else ""

