class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                curr = asteroid
                while True:
                    if curr < 0 and stack[-1] > 0:
                        a = stack.pop()
                        if a - abs(curr) > 0:
                            stack.append(a)
                        elif a - abs(curr) < 0:
                            stack.append(curr)
                        if len(stack) <= 1:
                            break
                        curr = stack.pop()
                    else:
                        stack.append(curr)
                        break
                        
        return stack
                    