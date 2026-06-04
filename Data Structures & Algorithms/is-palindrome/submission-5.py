class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = s.lower().replace(' ', '').replace('?', '').replace('!', '').replace(',', '').replace("'", '').replace('.','').replace(':','').replace(';','')

      for i, c in enumerate(s):
            if s[i] != s[len(s) - i - 1]:
                  return False
      return True