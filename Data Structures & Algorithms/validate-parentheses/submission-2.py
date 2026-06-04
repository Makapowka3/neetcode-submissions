class Solution:
    def isValid(self, s: str) -> bool:
      dict_p = {')': '(', ']': '[', '}': '{'}
      stack = []
      for ch in s:
            if ch in dict_p and len(stack) == 0:
                  return False
            if ch in dict_p.values():
                  stack.append(ch)
            if ch in dict_p and stack[-1] == dict_p[ch]:
                  stack.pop()
            elif ch in dict_p and stack[-1] != dict_p[ch]:
                  stack.append(ch)
      if len(stack) == 0:
            return True
      else:
            return False