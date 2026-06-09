class Solution:
    def isValid(self, s: str) -> bool:
      brackets = {'}': '{', ']': '[', ')': '('}
      stack = []
      for par in s:
            if par in brackets.values():
                  stack.append(par)
            else:
                  if not stack or stack[-1] != brackets[par]:
                        return False
                  stack.pop()
      return not stack