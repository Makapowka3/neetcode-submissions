class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_index = {}
        res = -1

        for i, ch in enumerate(s):
            if ch in first_index:
                res = max(res, i - first_index[ch] - 1)
            else:
                first_index[ch] = i

        return res