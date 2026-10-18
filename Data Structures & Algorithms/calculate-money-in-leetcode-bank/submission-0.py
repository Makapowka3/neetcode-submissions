class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)

        res = 28 * weeks + 7 * weeks * (weeks - 1) // 2
        res += days * (2 * weeks + days + 1) // 2

        return res