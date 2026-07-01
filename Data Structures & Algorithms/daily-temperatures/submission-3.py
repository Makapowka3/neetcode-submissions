class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            stack = []

            for i in range(len(temperatures)):
                while stack:
                    if temperatures[i] > temperatures[stack[-1]]:
                        temperatures[stack[-1]] = i - stack[-1]
                        stack.pop()
                    else:
                        break
                stack.append(i)
            
            for index in stack:
                temperatures[index] = 0
                
            return temperatures
