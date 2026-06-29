class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words[1:]:
            current = Counter(word)

            for ch in common:
                common[ch] = min(common[ch], current[ch])

        res = []
        for ch, count in common.items():
            for _ in range(count):
                res.append(ch)

        return res