class Solution:
    def isValid(self, s: str) -> bool:
      brackets = {'}': '{', ']': '[', ')': '('}
      stack = []
      for par in s:
            if par in brackets.values():
                  stack.append(par)
            else:
                  if stack and stack[-1] == brackets[par]:
                        stack.pop()
                  else:
                        return False
      return not stack