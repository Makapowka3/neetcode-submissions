class Solution:
    def maxScore(self, s: str) -> int:
        ones_right = s.count("1")
        zeroes_left = 0
        res = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zeroes_left += 1
            else:
                ones_right -= 1

            res = max(res, zeroes_left + ones_right)

        return res