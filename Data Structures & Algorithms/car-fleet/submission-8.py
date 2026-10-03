class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        num_fleets = n
        if n == 1:
            return 1
        # n >= 2
        position_speed = [(position[i], speed[i]) for i in range(n)]
        # sort by position - since values of position are unique, the result is unique
        sorted_position_speed = sorted(position_speed, key=lambda x: x[0], reverse = True)
        # speed[A] > speed[B] --> collision at t = (pos[B] - pos[A])/(speed[A] - speed[B])
        stack = []
        stack_position = 0
        stack_speed = 0
        # for i in range(n):
        #     # v_A > v_B is always part of guaranteed collision
        #     # conditions for collision are easier than no collision
        #     curr_position, curr_speed = sorted_position_speed[i]
        #     if stack:
        #         stack_position, stack_speed = sorted_position_speed[stack[-1]]
        #     while (stack and curr_speed > stack_speed and curr_position + curr_speed * (stack_position - curr_position)/(curr_speed - stack_speed) <= target):
        #         sorted_position_speed[i] = stack_position, stack_speed
        #         index = stack.pop()
        #         num_fleets -= 1
        #         if stack:
        #             stack_position, stack_speed = sorted_position_speed[stack[-1]]
            
        #     stack.append(i)
        for i in range(n):
            curr_position, curr_speed = sorted_position_speed[i]
            curr_time = (target - curr_position) / curr_speed

            if stack and curr_time <= stack[-1]:
                num_fleets -= 1
            else:
                stack.append(curr_time)
        return num_fleets