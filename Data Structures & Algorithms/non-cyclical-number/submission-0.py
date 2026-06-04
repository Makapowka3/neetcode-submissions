class Solution:
    def isHappy(self, n: int) -> bool:
        sets = set()
        new_num = n
        while new_num != 1:
            new_num = 0
            for ch in str(n):
                  new_num += int(ch)**2
            n = new_num
            if new_num in sets:
                  return False
            else:
                  sets.add(new_num)
        return True