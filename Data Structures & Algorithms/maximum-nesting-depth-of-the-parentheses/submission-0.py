class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []

        res = 0
        for el in s:
            if el == ')':
                stack.pop()
            elif el == '(':
                stack.append(el)
                res = max(res, len(stack))
        
        return res