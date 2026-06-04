class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0
        car_dict = {}
        for i in range(len(position)):
            car_dict[position[i]] = speed[i]
        position.sort(reverse=True)
        stack = []
        for pos in position:
            time = (target - pos) / car_dict[pos]
            if stack:
                prev = stack[-1]
                if prev >= time:
                    continue
            stack.append(time)
        return len(stack)