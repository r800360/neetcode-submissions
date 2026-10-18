class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If gas accumulated from station start becomes negative at i, none of the stations from start to i are a valid starting point
        # Total gas is an invariant
        total_gas = 0
        current_tank = 0
        start = 0

        for i in range(len(gas)):
            tank = gas[i] - cost[i]
            total_gas += tank
            current_tank += tank

            if current_tank < 0:
                # No station from start to i is valid
                start = i + 1
                current_tank = 0

        return start if total_gas >= 0 else -1