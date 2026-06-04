class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            alive = True

            while alive and stack and stack[-1] > 0 and a < 0:
                if stack[-1] < -a:          # top explodes
                    stack.pop()
                    continue
                elif stack[-1] == -a:       # both explode
                    stack.pop()
                alive = False               # current asteroid explodes (in both >= cases)

            if alive:
                stack.append(a)

        return stack