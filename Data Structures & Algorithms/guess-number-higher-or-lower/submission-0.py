# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower, upper = 0, n
        while lower <= upper:
            middle = (lower + upper) // 2
            if guess(middle) == 0:
                return middle
            elif guess(middle) == -1:
                upper = middle - 1
            else:
                lower = middle + 1
        