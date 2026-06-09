class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', ']': '[', '}': '{'}
        stack = []

        for par in s:
            if par in brackets:
                if not stack or stack[-1] != brackets[par]:
                    return False
                stack.pop()
            else:
                stack.append(par)

        return not stack