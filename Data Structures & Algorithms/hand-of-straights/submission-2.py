class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        frequencies = defaultdict(int)
        for value in hand:
            frequencies[value] += 1
        
        sorted_values = sorted(frequencies)

        for value in sorted_values:
            while frequencies[value] > 0:
                # Start a group with the smallest available value
                for x in range(value, value + groupSize):
                    if frequencies[x] == 0:
                        return False
                    frequencies[x] -= 1
        
        return True