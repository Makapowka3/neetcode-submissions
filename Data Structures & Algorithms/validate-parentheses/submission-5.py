class Solution:
    def isValid(self, s: str) -> bool:
      dict_p = {')': '(', ']': '[', '}': '{'}
      stack = []
      for ch in s:
            if ch in dict_p.values():
                  stack.append(ch)
            else:
                  if not stack or stack[-1] != dict_p[ch]:
                        return False
                  stack.pop()
      return not stack