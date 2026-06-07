class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_d = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for ch in text:
            if ch in balloon_d:
                balloon_d[ch] += 1
        balloon_d['o'] = balloon_d['o'] // 2
        balloon_d['l'] = balloon_d['l'] // 2
        max_words = len(text)
        for letter in balloon_d:
            max_words = min(max_words, balloon_d[letter])
        return max_words
        