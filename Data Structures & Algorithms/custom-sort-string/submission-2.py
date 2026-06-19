class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = []

        for ch in order:
            res.append(ch * count[ch])
            count[ch] = 0

        for ch, freq in count.items():
            res.append(ch * freq)

        return ''.join(res)