# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower, upper = 1, n
        while lower <= upper:
            middle = (lower + upper) // 2
            direction = guess(middle)
            if direction == 0:
                return middle
            elif direction == 1:
                lower = middle + 1
            else:
                upper = middle - 1

        