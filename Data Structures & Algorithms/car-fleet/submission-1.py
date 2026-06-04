class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0
        time_dict = {}
        car_dict = {}
        for i in range(len(position)):
            car_dict[position[i]] = speed[i]
        position.sort(reverse=True)
        stack = []
        for pos in position:
            time_dict[pos] = (target - pos) / car_dict[pos]
            if stack:
                prev = stack[-1]
                if time_dict[prev] >= time_dict[pos]:
                    continue
            stack.append(pos)
        return len(stack)