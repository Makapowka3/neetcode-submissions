class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            crushed = False
            while stack:
                if stack[-1] > 0:
                    if a > 0:
                        break
                    else:
                        if stack[-1] < abs(a):
                            stack.pop()
                        elif stack[-1] == abs(a):
                            stack.pop()
                            crushed = True
                            break
                        else:
                            crushed = True
                            break
                else:
                    break
            if not crushed:
                stack.append(a)
            
        return stack