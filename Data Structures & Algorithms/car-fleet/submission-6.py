class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashmap = {}
        for i in range(len(position)):
            hashmap[position[i]] = speed[i]
        
        position.sort(reverse=True)
        
        stack = []
        for i in range(len(position)):
            time = (target - position[i]) / hashmap[position[i]]
            if stack:
                if time <= stack[-1]:
                    continue
                else:
                    stack.append(time)
            else:
                stack.append(time)

        return len(stack)