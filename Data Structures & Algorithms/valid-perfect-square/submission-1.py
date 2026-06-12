class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lower, upper = 0, num
        while lower <= upper:
            middle = (lower + upper) // 2
            if middle * middle == num:
                return True
            elif middle * middle <= num:
                lower = middle + 1
            else:
                upper = middle - 1
        return False