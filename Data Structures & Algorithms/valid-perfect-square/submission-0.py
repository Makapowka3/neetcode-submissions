class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lower, upper = 0, num
        while lower <= upper:
            middle = (lower + upper) // 2
            square = middle * middle
            if square == num:
                return True
            elif square < num:
                lower = middle + 1
            else:
                upper = middle - 1
        return False