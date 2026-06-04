class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pairs.values():          # opening bracket
                stack.append(ch)
            else:                             # closing bracket
                # if stack empty or top doesn't match → invalid
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        return not stack