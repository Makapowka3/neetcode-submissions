class Solution:
    def arrangeCoins(self, n: int) -> int:
        lower, upper = 0, n
        while lower <= upper:
            middle = (lower + upper) // 2
            if middle * (middle + 1) // 2 == n:
                return middle
            elif middle * (middle + 1) // 2 < n:
                lower = middle + 1
            else:
                upper = middle - 1
        return upper