class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # O(m) time and O(1) space
        frequencies = [0] * 26

        for task in tasks:
            frequencies[ord(task) - ord("A")] += 1

        largest_frequency = max(frequencies)
        counter = frequencies.count(largest_frequency)

        return max(len(tasks), (largest_frequency - 1) * (n + 1) + counter)