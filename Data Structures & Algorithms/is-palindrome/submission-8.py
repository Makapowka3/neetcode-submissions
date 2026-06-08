class Solution:
    def isPalindrome(self, s: str) -> bool:
      snew = ''
      for ch in s:
            if ch.isalnum():
                  snew += ch.lower()

      for i, c in enumerate(snew):
            if snew[i] != snew[len(snew) - i - 1]:
                  return False
      return True