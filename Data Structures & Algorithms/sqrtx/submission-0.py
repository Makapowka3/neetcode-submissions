class Solution:
    def mySqrt(self, x: int) -> int:
        lower, upper = 0, x
        while lower <= upper:
            middle = (lower + upper) // 2
            if middle * middle == x:
                return middle
            elif middle * middle > x:
                upper = middle - 1
            else:
                lower = middle + 1
        return upper