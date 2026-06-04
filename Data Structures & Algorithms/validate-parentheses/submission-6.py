class Solution:
    def isValid(self, s: str) -> bool:
      hashmap = {')':'(', ']': '[', '}': '{'}
      stack = []
      for ch in s:
            if ch in hashmap.values():
                  stack.append(ch)
            else:
                  if not stack or stack[-1] != hashmap[ch]:
                        return False
                  stack.pop()
      return not stack
                        
                  