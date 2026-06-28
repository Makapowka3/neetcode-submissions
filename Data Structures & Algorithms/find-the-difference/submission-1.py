class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)

        for ch in count_t:
            if count_t[ch] > count_s[ch]:
                return ch