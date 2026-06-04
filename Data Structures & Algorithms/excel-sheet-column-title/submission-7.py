class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1              # shift to 0-indexed
            res.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26

        return ''.join(reversed(res))