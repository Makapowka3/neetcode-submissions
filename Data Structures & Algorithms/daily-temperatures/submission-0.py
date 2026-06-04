class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = len(temperatures) * [0]
        i = 0
        for temp in temperatures:
            if not stack:
                stack.append(i)
                i += 1
            else:
                if temperatures[stack[-1]] > temp:
                    stack.append(i)
                    i += 1
                else:
                    while stack and temp > temperatures[stack[-1]]:
                        pos = stack.pop()
                        res[pos] = i - pos
                    stack.append(i)
                    i += 1
        return res